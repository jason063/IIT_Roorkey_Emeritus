"""Week 1 demo — temperature changes variability, not facts.

Feature: run the same prompt at a low and a high temperature, a few times each,
and see determinism vs variety.
Run alone:  python demo_temperature.py
Run all:    python run.py
"""
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = OpenAI()

QUESTION = "Give a one-line tagline for a coffee shop."


def ask(temperature: float) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": QUESTION}],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def main():
    print("Feature: temperature controls how much the output varies.\n")
    print(f"Question: {QUESTION}\n")
    for temp in (0.0, 1.2):
        print(f"--- temperature = {temp} (3 runs) ---")
        for _ in range(3):
            print(f"  {ask(temp)}")
        print()


if __name__ == "__main__":
    main()
