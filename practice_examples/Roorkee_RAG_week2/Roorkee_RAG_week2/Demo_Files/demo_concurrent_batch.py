"""Week 2 demo — many calls at once with asyncio.gather.

Feature: ask several questions SEQUENTIALLY (one after another) vs CONCURRENTLY
(all at once with asyncio.gather), and time both. Concurrent time is bounded by
the slowest single call, not the sum.

Run:  python demo_concurrent_batch.py
"""
import asyncio
import time

from openai import AsyncOpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = AsyncOpenAI()

QUESTIONS = [
    "What is RAG in one sentence?",
    "Why might an LLM hallucinate?",
    "What does temperature do in an LLM call?",
    "What is an embedding?",
    "What is a vector database used for?",
]


async def ask(question: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        temperature=0.3,
    )
    return response.choices[0].message.content


async def _main() -> None:
    print("Feature: sequential vs concurrent (asyncio.gather).\n")

    start = time.perf_counter()
    for q in QUESTIONS:
        await ask(q)
    sequential = time.perf_counter() - start
    print(f"Sequential ({len(QUESTIONS)} calls): {sequential:.1f} s")

    start = time.perf_counter()
    await asyncio.gather(*(ask(q) for q in QUESTIONS))
    concurrent = time.perf_counter() - start
    print(f"Concurrent (asyncio.gather):     {concurrent:.1f} s")

    if concurrent > 0:
        print(f"\n-> about {sequential / concurrent:.1f}x faster, same calls, same answers.")


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
