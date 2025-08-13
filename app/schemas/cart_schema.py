from sqlmodel import SQLModel, Field
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

