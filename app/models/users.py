from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    articles = relationship("Article", back_populates="author")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, is_admin={self.is_admin})>"

    def create_user(self, db, user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
