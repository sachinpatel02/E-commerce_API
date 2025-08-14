from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class User(BaseModel):
    email: EmailStr

class UserRegister(User):
    first_name: str
    last_name: str
    password: str
    mobile_number: Annotated[str | None, Field(min_length=10)] = None

class UserLogin(User):
    password: str

class UserProfile(User):
    first_name: str
    last_name: str
    mobile_number: str

class UserUpdate(UserProfile):
    email: EmailStr | None
    first_name: str | None
    last_name: str | None
    mobile_number: str | None