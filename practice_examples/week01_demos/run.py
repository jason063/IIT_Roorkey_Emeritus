"""Week 1 demos — run every feature demo in order.

Usage:  python run.py
Each demo also runs on its own, e.g.  python demo_first_call.py

Later weeks carry forward the files they build on, so each week's folder stays
self-contained and runs end to end on Vocareum.
"""
import importlib
import os
import sys
from dotenv import load_dotenv

DEMOS = [
    ("demo_first_call", "Your first LLM call"),
    ("demo_system_prompt", "One system prompt = the biggest lever"),
    ("demo_response_object", "Reading the response object (tokens, latency, cost)"),
    ("demo_temperature", "Temperature changes variability, not facts"),
]


def main():
    load_dotenv()  # Load .env file if present
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.")
        print("On Vocareum: open a fresh terminal (the key is pre-set).")
        print("Off Vocareum: put your key in a .env file next to these demos.")
        sys.exit(1)

    for i, (module_name, title) in enumerate(DEMOS, 1):
        print("\n" + "=" * 72)
        print(f"  {i}. {title}")
        print("=" * 72)
        importlib.import_module(module_name).main()

    print("\n" + "=" * 72)
    print("  All Week 1 demos complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
