from sqlalchemy.orm import Session

from app.core.security import get_password_hash
from app.models import User
from app.schemas import UserCreate


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_create: UserCreate) -> User:
    user = User(
        email=user_create.email,
        hashed_password=get_password_hash(user_create.password),
        is_admin=user_create.is_admin,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user: User, user_update: UserCreate) -> User:
    user.email = user_update.email
    user.hashed_password = user_update.hashed_password
    user.is_admin = user_update.is_admin
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user
