from sqlalchemy.orm import Session

from app.models import Article
from app.schemas import ArticleCreate, ArticleUpdate


def get_article(db: Session, article_id: int) -> Article:
    return db.query(Article).filter(Article.id == article_id).first()


def get_articles(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> list:
    return (
        db.query(Article)
        .filter(Article.author_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_article(db: Session, article_create: ArticleCreate) -> Article:
    article = Article(**article_create.dict())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def update_article(
    db: Session, article: Article, article_update: ArticleUpdate
) -> Article:
    for field, value in article_update.dict(exclude_unset=True).items():
        setattr(article, field, value)
    db.commit()
    db.refresh(article)
    return article


def delete_article(db: Session, article_id: int) -> Article:
    article = db.query(Article).filter(Article.id == article_id).first()
    db.delete(article)
    db.commit()
    return article
