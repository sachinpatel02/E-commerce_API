from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4


class Category(SQLModel, table=True):
    """
    Category table
    """
    __tablename__ = "categories"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    name: str = Field(index=True, unique=True, max_length=100)
    description: str | None = Field(max_length=255)

    # Relationship creation
    # This will have 1 - to - many Relationship
    # one Category can have multiple Products

