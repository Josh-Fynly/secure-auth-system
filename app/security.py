import bcrypt
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def hash_password(password: str):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def verify_password(password: str, hashed: str):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )

def create_access_token(data: dict):
    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow() + timedelta(minutes=15)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
