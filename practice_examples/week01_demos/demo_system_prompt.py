"""Week 1 demo — the system prompt is the biggest lever.

Feature: send the SAME question through different system prompts and watch the
voice change completely while the underlying facts stay the same.
Run alone:  python demo_system_prompt.py
Run all:    python run.py
"""
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = OpenAI()

QUESTION = "Explain quantum entanglement in two sentences."

SYSTEM_PROMPTS = {
    "Concise": "You are concise.",
    "Kindergarten teacher": "You are a kindergarten teacher. Explain like the listener is five years old.",
    "Shakespearean poet": "You are a Shakespearean poet. Reply in iambic verse where possible.",
    "Impatient physicist": "You are a brilliant but impatient physicist. Accurate, but no niceties.",
}


def ask(system_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": QUESTION},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


def main():
    print("Feature: one system prompt = the biggest change you can make.\n")
    print(f"Question (held constant): {QUESTION}\n")
    for label, system_prompt in SYSTEM_PROMPTS.items():
        print(f"--- {label} ---")
        print(ask(system_prompt))
        print()


if __name__ == "__main__":
    main()
