"""Week 2 demo — Pydantic: typed shapes you can trust.

Three sections in one run:
  1. a basic model (+ type coercion)
  2. what a ValidationError actually looks like
  3. parsing an LLM JSON response into a typed object

Run:  python demo_pydantic.py
"""
import json
from typing import Optional

from pydantic import BaseModel, ValidationError


def _banner(title: str) -> None:
    print("\n" + "=" * 70 + f"\n  {title}\n" + "=" * 70)


class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None


class ExpectedAnswer(BaseModel):
    summary: str
    confidence: float
    sources: list[str]


def main():
    print("Feature: Pydantic validates data shapes at runtime.")

    _banner("1. A basic model (+ coercion)")
    u = User(name="Asha", age=29)
    print(f"  User(...).model_dump() -> {u.model_dump()}")
    u2 = User(name="Bo", age="30")          # note: the string '30' is coerced to int
    print(f"  age from '30' -> {u2.age!r} ({type(u2.age).__name__})")

    _banner("2. When bad data goes in")
    try:
        User(name="Asha", age="not a number")
    except ValidationError as exc:
        print(exc)
    print("  -> which field (age), why (int_parsing), what you sent. No silent corruption.")

    _banner("3. Parse an LLM JSON response")
    good = json.dumps({"summary": "RAG grounds answers in your docs.",
                       "confidence": 0.9, "sources": ["doc1", "doc2"]})
    print(f"  well-formed -> {ExpectedAnswer.model_validate_json(good)}")
    bad = json.dumps({"summary": "x", "confidence": "high", "sources": ["doc1"]})
    try:
        ExpectedAnswer.model_validate_json(bad)     # 'high' is not a float
    except ValidationError as exc:
        print("  malformed ->")
        print(exc)
    print("\n  Takeaway: catch off-shape LLM output at the door, not 3 calls later.")


if __name__ == "__main__":
    main()
