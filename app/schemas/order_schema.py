from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Optional


class Order(SQLModel, table=True):
    """
    Order table
    """
    __tablename__ = "orders"
    id: UUID = Field(primary_key=True, default_factory=uuid4, index=True)
    status: str = Field(default="pending", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # foreign keys
    user_id: UUID = Field(foreign_key="users.id")

    # Relationship creation
    user : Optional["User"] = Relationship(back_populates="orders")
    payment: Optional["Payment"] = Relationship(back_populates="orders")
