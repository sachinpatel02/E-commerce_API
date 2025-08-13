from sqlmodel import SQLModel, Field, Relationship, Column, DECIMAL
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
    order: "Order" = Relationship(back_populates="items")
    product: "Product" = Relationship()  # no back_populates as there isn't any Rel field in Products for OrderItems
