"""Week 2 demos — run every feature demo in order.

Usage:  python run.py
Each demo also runs on its own, e.g.  python demo_pydantic.py

Demos marked (needs key) call the real OpenAI API; the rest use a local fake LLM.
If no OPENAI_API_KEY is set, the real-API demos are skipped with a note.
"""
import importlib
import os

DEMOS = [
    ("demo_first_call",      "Recap: one sync call (from Week 1)", True),
    ("demo_pydantic",        "Pydantic: typed shapes you can trust", False),
    ("demo_async_call",      "The same call, now async", True),
    ("demo_concurrent_batch","Many calls at once (asyncio.gather)", True),
    ("demo_retries",         "Retry with exponential backoff", False),
    ("demo_pipeline",        "The whole pipeline, tied together", False),
]


def main():
    has_key = bool(os.getenv("OPENAI_API_KEY"))
    if not has_key:
        print("Note: OPENAI_API_KEY not set — real-API demos will be skipped.")
        print("On Vocareum, open a fresh terminal to get the key.\n")

    for i, (module_name, title, needs_key) in enumerate(DEMOS, 1):
        print("\n" + "=" * 72)
        print(f"  {i}. {title}" + ("   (needs key)" if needs_key else ""))
        print("=" * 72)
        if needs_key and not has_key:
            print("  skipped (no OPENAI_API_KEY).")
            continue
        importlib.import_module(module_name).main()

    print("\n" + "=" * 72 + "\n  All Week 2 demos complete.\n" + "=" * 72)


if __name__ == "__main__":
    main()
