from sqlalchemy.orm import Session
from . import models, security

MAX_FAILED_ATTEMPTS = 5

def register_user(db: Session, username: str, password: str):

    hashed = security.hash_password(password)

    user = models.User(
        username=username,
        password=hashed
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def authenticate_user(db: Session, username: str, password: str):

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

    if not user:
        return None, "User not found"

    if user.is_locked:
        return None, "Account locked"

    if not security.verify_password(password, user.password):

        user.failed_attempts += 1

        if user.failed_attempts >= MAX_FAILED_ATTEMPTS:
            user.is_locked = True

        db.commit()

        return None, "Invalid credentials"

    user.failed_attempts = 0
    db.commit()

    return user, None
