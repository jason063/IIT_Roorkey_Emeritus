"""Week 2 demo — carried forward from Week 1: a single (sync) LLM call.

This is where we start: last week we made ONE call. This week we make MANY,
in parallel, validated, with retries. Run this to remind yourself of the baseline.

Run:  python demo_first_call.py
"""
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = OpenAI()


def main():
    print("Feature (recap from W1): one synchronous LLM call.\n")
    question = "What is RAG in one sentence?"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    print(f"Q: {question}")
    print(f"A: {response.choices[0].message.content}")


if __name__ == "__main__":
    main()
