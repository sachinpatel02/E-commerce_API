"""
session.py
    * create a database engine
    * create database and tables using schemas
    * create a session for CRUD operations on database
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import create_engine, Session, SQLModel

from app.core.config import configs

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
