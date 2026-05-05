from sqlalchemy.orm import Session
from . import models, security

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
