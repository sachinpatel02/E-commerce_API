from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import configs
from app.schemas import address_schema

# Database URL from your configuration
DATABASE_URL = configs.DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debugging SQL


def create_db_and_tables():
    print("Attempting to create database tables...")
    try:
        # Ensure all SQLModel models are imported before this call
        SQLModel.metadata.create_all(engine)
        print("SQLModel Metadata:", SQLModel.metadata)
        print("✅ Database and tables created successfully")
    except SQLAlchemyError as e:
        print(f"❌ Failed to create/connect database and tables: {str(e)}")
        raise  # Re-raise the exception for further debugging


def create_session():
    # Create a session for database operations
    with Session(engine) as session:
        yield session
