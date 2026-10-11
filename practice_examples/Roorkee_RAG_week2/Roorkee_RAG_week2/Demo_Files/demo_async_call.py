"""Week 2 demo — the same call, now async.

Feature: rewrite last week's call with AsyncOpenAI. Three keywords are the whole
mental model:
    async def   -> declares an awaitable coroutine
    await       -> pause THIS coroutine until the call returns
    asyncio.run -> start the event loop

Run:  python demo_async_call.py
"""
import asyncio

from openai import AsyncOpenAI

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

client = AsyncOpenAI()


async def ask(question: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


async def _main() -> None:
    print("Feature: one async LLM call (async def / await / asyncio.run).\n")
    question = "Explain async and await in plain language."
    print(f"Q: {question}")
    print(f"A: {await ask(question)}")


def main() -> None:
    asyncio.run(_main())


if __name__ == "__main__":
    main()
