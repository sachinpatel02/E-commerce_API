from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

class UserIn(User):
    password: str
    mobile_number: Annotated[str | None, Field(min_length=10)] = None