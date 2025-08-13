from sqlmodel import SQLModel, Field, Column, DECIMAL
from uuid import UUID, uuid4
from datetime import datetime, timezone


class Payment(SQLModel, table=True):
    """
    Payment table
    """
    __tablename__ = "payments"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    transaction_id: str = Field(unique=True, index=True)
    status: str = Field(index=True)
    amount: float = Field(sa_column=Column(DECIMAL(10, 2)))
    currency: str
    payment_method: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    # Foreign Keys
    order_id: UUID = Field(foreign_key="orders.id")

    # Relationships

