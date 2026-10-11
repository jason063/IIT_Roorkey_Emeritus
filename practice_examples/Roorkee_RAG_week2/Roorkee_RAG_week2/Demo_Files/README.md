# Week 2 — Teaching Demos

Small, self-contained Python demos for Week 2 (Pydantic, async, concurrency).
No `src/` package, no web UI — just scripts you run in the Vocareum terminal.

## Setup

    pip install --break-system-packages openai python-dotenv pydantic

On Vocareum the OpenAI key is already set. Off Vocareum, put it in a `.env` file.

## Run everything

    python run.py

## Or run one feature at a time

| File | Shows | Calls |
|------|-------|-------|
| `demo_first_call.py` | Recap: one sync call (carried from Week 1) | real API |
| `demo_pydantic.py` | Typed shapes, coercion, validation, parsing LLM JSON | none |
| `demo_async_call.py` | The same call rewritten async | real API |
| `demo_concurrent_batch.py` | Sequential vs `asyncio.gather` — the speedup | real API |
| `demo_retries.py` | Retry with exponential backoff (1s, 2s, 4s) | fake LLM |
| `demo_pipeline.py` | Read CSV -> batched concurrent calls + retry -> JSON logs | fake LLM |

`fake_llm.py` is a quota-free async stand-in with a `fail_rate` knob, so the
retry/pipeline demos show failures reliably. `questions.csv` holds sample questions.

## Carry-forward

`demo_first_call.py` comes from Week 1 (one call). This week grows it into many
calls, in parallel, validated, with retries. `fake_llm.py` is introduced here and
will carry forward to later weeks that need a quota-free LLM.
