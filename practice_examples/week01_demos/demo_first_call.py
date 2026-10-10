import os
import sys
from openai import OpenAI

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

def main():
    print("Feature: your first LLM call — one question in, one answer out.\n")

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
