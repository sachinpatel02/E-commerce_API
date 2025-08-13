from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import configs
from app.schemas.address_schema import Address
from app.schemas.user_schema import User
from app.schemas.order_schema import Order
from app.schemas.cart_schema import Cart
from app.schemas.cart_item_schema import CartItem
from app.schemas.categories_schema import Category
from app.schemas.order_item_schema import OrderItem
from app.schemas.payments_schema import Payment
from app.schemas.product_schema import Product
from app.schemas import relationships

# Database URL from your configuration
DATABASE_URL = configs.DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debugging SQL


def create_db_and_tables():
    print("Attempting to create database tables...")
    try:
        SQLModel.metadata.create_all(engine)
        print("Registered tables:", SQLModel.metadata.tables.keys())
        print("✅ Database and tables created successfully")
    except SQLAlchemyError as e:
        print(f"❌ Failed to create/connect database and tables: {str(e)}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error during table creation: {str(e)}")
        raise

def create_session():
    # Create a session for database operations
    with Session(engine) as session:
        yield session
