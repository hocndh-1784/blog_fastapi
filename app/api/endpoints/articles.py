from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.core.db import get_db
from app.core.security import get_current_user
from app.crud.articles import (create_article, delete_article, get_article,
                               get_articles, update_article)
from app.models import User

articles_router = APIRouter()


@articles_router.get("/users/{user_id}/articles", response_model=List[schemas.Article])
def get_user_articles(
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    articles = get_articles(db=db, user_id=user_id, skip=skip, limit=limit)
    if not articles:
        raise HTTPException(status_code=404, detail="No articles found for this user")
    return articles


@articles_router.post("/articles", response_model=schemas.Article)
def create_new_article(
    article_create: schemas.ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    article = create_article(db=db, article_create=article_create)
    return article


@articles_router.get("/articles/{article_id}", response_model=schemas.Article)
def get_single_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    article = get_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article


@articles_router.put("/articles/{article_id}", response_model=schemas.Article)
def update_single_article(
    article_id: int,
    article_update: schemas.ArticleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    article = get_article(db=db, article_id=article_id)
    if article.author_id != current_user.id or not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="You don't have access to this article"
        )
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    article = update_article(db=db, article=article, article_update=article_update)
    return article


@articles_router.delete("/articles/{article_id}")
def delete_single_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    article = get_article(db=db, article_id=article_id)
    if article.author_id != current_user.id or not current_user.is_admin:
        raise HTTPException(
            status_code=403, detail="You don't have access to this article"
        )
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    delete_article(db=db, article=article)
    return {"message": "Article deleted successfully"}
