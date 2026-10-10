import asyncio

from openai import AsyncOpenAI


async def ask(question: str) -> str:
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content


async def main() -> None:
    response = await ask("What is the capital of France?")
    response2 = await ask("What is the capital of Germany?")
    response3 = await ask("What is the capital of Italy?")
    response4 = await ask("What is the capital of Spain?")
    response5 = await ask("What is the capital of Portugal?")

    print(response)
    print(response2)
    print(response3)
    print(response4)
    print(response5)


if __name__ == "__main__":
    main()
    asyncio.run(main())   #Actual parallel execution #we will gather print function parallel as well as print fucntion will never run in sequential.
