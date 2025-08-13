
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

class Address(SQLModel, table=True):
    """
    Address table
    """
    __tablename__ = "addresses"
    id: UUID = Field(primary_key=True, default_factory=uuid4, index=True)
    street: str
    city: str
    state: str
    country: str
    postal_code: str
    is_default_shipping: bool
    is_default_billing: bool

    # Foreign Key
    user_id: UUID = Field(foreign_key="users.id")

    # Relationship creation

