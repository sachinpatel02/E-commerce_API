from fastapi import FastAPI
from .db.session import create_db_and_tables
app = FastAPI()

@app.on_event("startup")
async def startup():
    print("♻️Database initialization started...")
    create_db_and_tables()
@app.get("/")
async def root():
    return {"message": "Hello World"}