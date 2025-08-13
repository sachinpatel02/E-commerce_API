from typing import Optional

from sqlmodel import SQLModel, Field, Column, DECIMAL, Relationship
from uuid import UUID, uuid4


class OrderItem(SQLModel, table=True):
    """
    OrderItem table
    """
    __tablename__ = "order_items"
    id: UUID = Field(primary_key=True, default_factory=uuid4, index=True)
    quantity: int
    price_at_purchase: float = Field(sa_column=Column(DECIMAL(10, 2)))

    # Foreign keys
    order_id: UUID = Field(foreign_key="orders.id")
    product_id: UUID = Field(foreign_key="products.id")

    # Relationship creation
    product : Optional["Product"] = Relationship(back_populates="items")

