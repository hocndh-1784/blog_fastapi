from fastapi import APIRouter

from app.api.endpoints import articles_router, users_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(articles_router, prefix="/articles", tags=["articles"])
