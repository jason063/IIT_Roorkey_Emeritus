import asyncio

async def hello():
    await asyncio.sleep(1)
    return f"Hello, World!"

asyncio.run(hello())



import httpx   # it si ssync call  replace for async from request-------request is sync call and https is async client

async def fetch_data():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
        return response.json()


