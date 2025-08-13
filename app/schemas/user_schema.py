from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from pydantic import EmailStr
from datetime import datetime, timezone
from typing import ClassVar, Optional


class User(SQLModel, table=True):
    """
    User table
    """
    __tablename__: ClassVar[str] = 'users'
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    email: EmailStr = Field(unique=True, index=True)
    hashed_password: str = Field(nullable=False)
    first_name: str = Field(nullable=False, max_length=50)
    last_name: str = Field(nullable=False, max_length=50)
    mobile_number: Optional[str] = Field(nullable=False, unique=True, index=True, max_length=20)
    is_active: bool = Field(default=True, nullable=False)
    is_admin: bool = Field(default=False, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)


