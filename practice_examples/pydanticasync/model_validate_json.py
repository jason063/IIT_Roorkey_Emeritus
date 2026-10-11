from wsgiref.validate import validator

from typing import Optional
from pydantic import BaseModel, ValidationError
import json


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

raw = '{"summary":"", "confidence":0.8, "sources":["source1"]}'


test = json.dumps(raw)
try:
    expected_answer = ExpectedAnswer.parse_raw(raw)
    print(expected_answer)
except ValidationError as e:
    print(f"Error parsing raw data: {e}")