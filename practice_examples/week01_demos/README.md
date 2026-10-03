# Week 1 — Teaching Demos

Small, self-contained Python demos an instructor runs live to show the Week 1 features.
No `src/` package and no web UI — just scripts you run in the Vocareum terminal.

## Setup

    pip install --break-system-packages openai python-dotenv

On Vocareum the OpenAI key is already set. Off Vocareum, put it in a `.env` file next to these files.

## Run everything

    python run.py

## Or run one feature at a time

| File | Shows |
|------|-------|
| `demo_first_call.py` | A single LLM call, end to end |
| `demo_system_prompt.py` | How one system prompt changes the whole voice |
| `demo_response_object.py` | Reading the response object — tokens, latency, estimated cost |
| `demo_temperature.py` | How temperature changes variability, not facts |

## Model & cost

All demos use `gpt-4o-mini` — fast, and a fraction of a cent per call.

## Carry-forward

This is Week 1, so nothing is carried in. From Week 2 on, each week's folder includes a
copy of any earlier demo it builds on, so every week stays self-contained and runnable.
