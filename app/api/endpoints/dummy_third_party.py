from fastapi import APIRouter, Depends
from services import get_dummy_user

from app.core.security import get_current_user
from app.models.users import User

articles_router = APIRouter()


@articles_router.get("/third_party/users/{user_id}")
def get_user_in_third_party(
    user_id: int, current_user: User = Depends(get_current_user)
):
    user_data = get_dummy_user(user_id=user_id)
    return user_data
