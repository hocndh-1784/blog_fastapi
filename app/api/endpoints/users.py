from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.core.db import get_db
from app.core.security import authenticate_user, create_access_token
from app.crud import create_user, get_user

users_router = APIRouter()


@users_router.post("/register", response_model=schemas.User)
def register_user(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    user = get_user(db=db, email=user_create.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = create_user(db=db, user_create=user_create)
    return user


@users_router.post("/login", response_model=schemas.Token)
def login_user(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(
        db=db, username=user_login.username, password=user_login.password
    )
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
