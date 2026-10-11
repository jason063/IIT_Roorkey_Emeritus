import os
import sys
from typing import Optional
from openai import OpenAI
from pydantic import BaseModel, ValidationError
import json

try:
    from dotenv import load_dotenv
    load_dotenv()  # loads OPENAI_API_KEY from .env off-Vocareum
except ImportError:
    pass


# Initialize client with Vocareum base URL
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openai.vocareum.com/v1"
)

class ExpectedAnswer(BaseModel):
    """
    ExpectedAnswer is a Pydantic model that represents the expected answer for a given question.
    It contains the following fields:
    - answer: The expected answer as a string.
    - confidence: The confidence level of the expected answer as a float between 0 and 1.
    - source: The source of the expected answer as a string (optional).
    """

    summary: str
    confidence: float
    sources: Optional[list[str]] = None

    # @validator('confidence')
    # def validate_confidence(cls, value):
    #     if not (0 <= value <= 1):
    #         raise ValueError('Confidence must be between 0 and 1.')
    #     return value


def main():
    print("Feature: your first LLM call — one question in, one answer out.\n")

    question = "What is RAG in one sentence?"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are helpful assistant which response with summary and confidence score between 0 and 1 in json format"},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    # try:
    #     expected_answer = ExpectedAnswer.parse_raw(response.choices[0].message.content)
    #     print(expected_answer)
    # except ValidationError as e:
    #     print(f"Error parsing raw data: {e}")

    print(f"Q: {question}")
    print(f"A: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
