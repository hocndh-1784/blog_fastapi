from fastapi import FastAPI

from .api.router import router
from .core.config import settings
from .core.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)

app.include_router(router)
