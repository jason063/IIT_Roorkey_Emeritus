import asyncio
from fake_llm import Question, fake_ask_llm, FakeLLMError


async def ask_with_retry(q, fail_rate=0.0, max_retries=4):
    for attempt in range(max_retries):
        try:
            return await fake_ask_llm(q, fail_rate=fail_rate)
        except FakeLLMError:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)


async def run_stream(questions, fail_rate=0.0):
    tasks = [ask_with_retry(q, fail_rate=fail_rate) for q in questions]
    results = []
    for coro in asyncio.as_completed(tasks):        # <-- the one change from gather
        try:
            ans = await coro
            print(f"  done: {ans.text[:55]}...")      # prints the instant it's ready
            results.append(ans)
        except FakeLLMError:
            print("  gave up on one call after all retries")
    return results


if __name__ == "__main__":
    import sys
    fail_rate = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    sample = [Question(text=t) for t in [
        "What is RAG in one sentence?",
        "Name three uses of vector databases.",
        "Why might an LLM hallucinate?",
        "Explain async and await in plain language.",
        "What is exponential backoff?",
    ]]
    print(f"\nrun_stream — fail_rate={fail_rate}")
    answers = asyncio.run(run_stream(sample, fail_rate=fail_rate))
    print(f"\nreturned {len(answers)} answers")
