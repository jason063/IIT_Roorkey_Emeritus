from pydantic import BaseModel, Field
from typing import List, Optional

class User(BaseModel):
    id: int = Field(..., description="The unique identifier for the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email address of the user")
    is_active: bool = Field(default=True, description="Indicates if the user is active")
    roles: Optional[List[str]] = Field(default=None, description="List of roles assigned to the user")

u = User(id="1", name="John Doe", email="john@example.com", roles=["admin", "user"])
print(u.model_dump())


"""

Assync : function will execute till the program complete the cycle or whenever async funciton input required
***
Validate inputs
Validate outputs and clean errors


Coersion in Pydantic 

Automatic parsing of string to integer for certain variables but not with every data type.


Number coersion works but nothing alike complete "stringggggg"

"""
