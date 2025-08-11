from sqlmodel import create_engine, Session, SQLModel

from ..core.config import configs

DATABASE_URL = configs.DATABASE_URL
engine = create_engine(DATABASE_URL)

def create_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
        print("✅Database/Tables created")
    except Exception(BaseException) as e:
        print("❌Failed to create/connect database and tables")