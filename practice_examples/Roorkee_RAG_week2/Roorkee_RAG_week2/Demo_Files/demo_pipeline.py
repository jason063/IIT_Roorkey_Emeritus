"""Week 2 demo — the whole pipeline, tied together.

Feature: read questions from a CSV, ask them in small BATCHES concurrently
(asyncio.gather), retry each with backoff, and emit one JSON log line per call.
Everything from this week in one flow. Uses fake_llm (no quota, reliable retries).

Run:  python demo_pipeline.py
"""
import asyncio
import csv
import json
import logging
import sys
import time
from pathlib import Path

from fake_llm import Question, Answer, fake_ask_llm, FakeLLMError

# --- one-JSON-record-per-line logger (to stderr) ---
log = logging.getLogger("pipeline")
log.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stderr)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps({"level": record.levelname, "msg": record.getMessage(),
                           "t": round(time.time(), 3)})


_handler.setFormatter(JsonFormatter())
log.addHandler(_handler)

BATCH_SIZE = 3
FAIL_RATE = 0.3


async def ask_with_retry(q: Question, max_retries: int = 4) -> Answer:
    for attempt in range(max_retries):
        try:
            answer = await fake_ask_llm(q, fail_rate=FAIL_RATE)
            log.info(f"asked: {q.text[:40]}")
            answer.retries = attempt
            return answer
        except FakeLLMError:
            if attempt == max_retries - 1:
                log.warning(f"gave up: {q.text[:40]}")
                raise
            log.warning(f"retry {attempt + 1} in {2 ** attempt}s: {q.text[:40]}")
            await asyncio.sleep(2 ** attempt)


async def run_batch(questions: list[Question]) -> list[Answer]:
    results: list[Answer] = []
    # batching: process BATCH_SIZE at a time, not all at once
    for i in range(0, len(questions), BATCH_SIZE):
        chunk = questions[i:i + BATCH_SIZE]
        answers = await asyncio.gather(*(ask_with_retry(q) for q in chunk))
        results.extend(answers)
        await asyncio.sleep(0.1)  # be a polite client between batches
    return results


def load_questions() -> list[Question]:
    path = Path(__file__).with_name("questions.csv")
    with path.open() as f:
        return [Question(text=row["text"]) for row in csv.DictReader(f)]


async def _main() -> None:
    print("Feature: read CSV -> batched concurrent calls + retry -> validated answers + JSON logs.\n")
    questions = load_questions()
    start = time.perf_counter()
    answers = await run_batch(questions)
    elapsed = time.perf_counter() - start
    print(f"\nGot {len(answers)} validated answers in {elapsed:.1f}s "
          f"(batch size {BATCH_SIZE}, fail rate {FAIL_RATE}):\n")
    for a in answers:
        print(f"  Q: {a.question[:55]}")
        print(f"  A: {a.text[:70]}...  (retries={a.retries})\n")


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
