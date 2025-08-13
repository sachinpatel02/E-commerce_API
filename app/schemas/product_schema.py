from sqlalchemy.orm import Relationship
from sqlmodel import Field, SQLModel, Column, DECIMAL
from uuid import UUID, uuid4


class Product(SQLModel, table=True):
    """
    Products table
    """
    __tablename__ = "products"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True, nullable=False)
    name: str = Field(index=True, nullable=False, max_length=100)
    description: str | None = Field(nullable=True)
    price: float = Field(sa_column=Column(DECIMAL(10, 2), nullable=False))
    stock_quantity: int = Field(nullable=False)
    is_active: bool = Field(nullable=False)

    # foreign keys
    category_id: UUID | None = Field(index=True, nullable=False, foreign_key="categories.id")

    # Relationship creation
    # this will have 1 - to - many relationship
    category: "Category" = Relationship(back_populates="products")
