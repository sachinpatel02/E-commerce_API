from typing import Optional

from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4


class Cart(SQLModel, table=True):
    """
    Cart table
    """
    __tablename__ = "carts"
    id: UUID = Field(default_factory=uuid4, primary_key=True)

    # foreign keys
    user_id: UUID = Field(foreign_key="users.id", unique=True)

    # Relationship
    user: Optional["User"] = Relationship(back_populates="carts")
    items: Optional["CartItem"] = Relationship(back_populates="cart")
