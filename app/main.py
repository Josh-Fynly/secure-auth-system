from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import schemas, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "auth system running"}

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = auth.register_user(db, user.username, user.password)
    return {"message": f"user {new_user.username} created"}
