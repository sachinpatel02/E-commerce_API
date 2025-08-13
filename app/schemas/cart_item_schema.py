from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4


class CartItem(SQLModel, table=True):
    """
    Cart Item table
    """
    __tablename__ = "cart_items"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    quantity: int

    # Foreign keys
    cart_id: int = Field(foreign_key="carts.id")
    product_id: UUID = Field(foreign_key="products.id")

    # Relationships
    cart: "Cart" = Relationship(back_populates="items")
    product: "Product" = Relationship()
