import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My FastAPI Project"
    log_level: str = "info"


settings = Settings()

load_dotenv(dotenv_path="../.env")

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
REFRESS_TOKEN_EXPIRE_DAYS = os.getenv("REFRESS_TOKEN_EXPIRE_MINUTES")
