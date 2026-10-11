import asyncio
from turtle import delay

async def call(i):
    await asyncio.sleep(1)
    return i ** 2

results = await asyncio.gather(*(call(i) for i in range(10)))

print(results)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# Batching

async def batched(items, size, fn):
    out =[]
    for i in range (0, len(items), size):
        batch = items[i:i+size]
        out+= await asyncio.gather(*(fn(item) for item in batch))
        await asyncio.sleep(0.1)  # Optional: Add a small delay between batches
    return out
        # out.extend(await asyncio.gather(*(fn(item) for item in batch)))


# retrying with exponential backoff

async def with_retry(fn, **args, tries=3):
    for attempt in range(tries):
        try:
            return await fn(**args)
        except Exception as e:
            if attempt ==  tries - 1: raise e
            await asyncio.sleep(2 ** attempt)  # Exponential backoff