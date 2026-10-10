import os
from openai import AsyncOpenAI
from typing import Optional
from pydantic import BaseModel, ValidationError

try:
    from dotenv import load_dotenv
    load_dotenv()  # loads OPENAI_API_KEY from .env off-Vocareum
except ImportError:
    pass

# Initialize client with Vocareum base URL
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openai.vocareum.com/v1"
)

class ExpectedAnswer(BaseModel):
    """
    ExpectedAnswer is a Pydantic model that represents the expected answer for a given question.
    It contains the following fields:
    - summary: The expected answer as a string.
    - confidence: The confidence level of the expected answer as a float between 0 and 1.
    - sources: The source(s) of the expected answer as a list of strings (optional).
    """

    summary: str
    confidence: float
    sources: Optional[list[str]] = None

async def main():
    print("Feature: your first LLM call — one question in, one answer out.\n")

    questions = [
        "what is rag in 500 tokens",
        "What is RAG in one sentence?",
    ]

    for question in questions:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are helpful assistant which responds with summary and confidence score between 0 and 1 in json format"},
                {"role": "user", "content": question},
            ],
            temperature=0.3,
        )
        print(f"Q: {question}")
        print(f"A: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
    # import asyncio
    # asyncio.run(main())
