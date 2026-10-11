"""Week 2 demo — retry with exponential backoff.

Feature: a flaky call (simulated with fail_rate) is retried, waiting 1s, then 2s,
then 4s between attempts. Uses fake_llm so the failures are reliable and free.

Run:  python demo_retries.py
"""
import asyncio

from fake_llm import Question, fake_ask_llm, FakeLLMError


async def ask_with_retry(q: Question, max_retries: int = 4) -> str:
    for attempt in range(max_retries):
        try:
            answer = await fake_ask_llm(q, fail_rate=0.6)  # 60% chance of a transient fail
            print(f"  attempt {attempt + 1}: success")
            return answer.text
        except FakeLLMError:
            wait = 2 ** attempt  # 1, 2, 4, 8 ...
            if attempt == max_retries - 1:
                print(f"  attempt {attempt + 1}: failed — giving up")
                raise
            print(f"  attempt {attempt + 1}: failed — retrying in {wait}s")
            await asyncio.sleep(wait)


async def _main() -> None:
    print("Feature: retry-with-backoff on a flaky call (waits 1s, 2s, 4s...).\n")
    q = Question(text="What is exponential backoff?")
    try:
        answer = await ask_with_retry(q)
        print(f"\nA: {answer}")
    except FakeLLMError:
        print("\nAll retries exhausted (unlucky run — try again).")


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
