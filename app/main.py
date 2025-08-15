"""
main.py
    * initiate database connection
    * create app instance
    * include api routers
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.user_router import user_router
from app.db.session import create_db_and_tables
from app.api.auth_router import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("♻️ Database initialization started...")
    create_db_and_tables()
    yield
    print("🛑 Application shutting down...")


app = FastAPI(lifespan=lifespan, prefix="/api")
app.include_router(auth_router)
app.include_router(user_router)
