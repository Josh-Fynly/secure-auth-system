from fastapi import FastAPI
from .database import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "database connected"}
