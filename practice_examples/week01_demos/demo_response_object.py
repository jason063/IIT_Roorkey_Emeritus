"""Week 1 demo — there is more in the response than just the text.

Feature: read the response object — token counts, latency, and an estimated
cost — the numbers behind the "what just happened" slide.
Run alone:  python demo_response_object.py
Run all:    python run.py
"""
import time
from openai import OpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = OpenAI()

# Approximate gpt-4o-mini pricing (USD per token). Prices change — check current rates.
PRICE_PER_INPUT_TOKEN = 0.15 / 1_000_000
PRICE_PER_OUTPUT_TOKEN = 0.60 / 1_000_000


def main():
    print("Feature: reading the response object — tokens, latency, cost.\n")
    question = "Why might an LLM hallucinate? Answer in two sentences."

    start = time.perf_counter()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    latency = time.perf_counter() - start

    usage = response.usage
    est_cost = (usage.prompt_tokens * PRICE_PER_INPUT_TOKEN
                + usage.completion_tokens * PRICE_PER_OUTPUT_TOKEN)

    print(f"Answer:            {response.choices[0].message.content}\n")
    print(f"Model:             {response.model}")
    print(f"Prompt tokens:     {usage.prompt_tokens}")
    print(f"Completion tokens: {usage.completion_tokens}")
    print(f"Total tokens:      {usage.total_tokens}")
    print(f"Latency:           {latency:.2f} s")
    print(f"Estimated cost:    ${est_cost:.6f}  (approx; prices change)")


if __name__ == "__main__":
    main()
