from fastapi import FastAPI
from core.config import settings

from db.session import lifespan

def start_application():
    app = FastAPI(
        lifespan=lifespan,
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
    return app

app = start_application()

@app.get("/")
async def root():
    return {"msg": "Bullet Journal"}