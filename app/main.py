from contextlib import asynccontextmanager

from fastapi import FastAPI

from .db.session import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("♻️ Database initialization started...")
    create_db_and_tables()
    yield
    print("🛑 Application shutting down...")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}
