from fastapi import FastAPI

from core.config import settings
from db.session import lifespan
from api.base import router

def include_router(app):
    app.include_router(router)

def start_application():
    app = FastAPI(
        lifespan=lifespan,
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    include_router(app)
    return app

app = start_application()

