from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
