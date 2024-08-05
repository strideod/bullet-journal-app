from fastapi import FastAPI
from pymongo import MongoClient
from contextlib import asynccontextmanager

from core.config import settings

ATLAS_DATABASE_URI = settings.ATLAS_URI
ATLAS_DB_NAME = settings.DB_NAME


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    app.mongodb_client = MongoClient(ATLAS_DATABASE_URI)
    app.database = app.mongodb_client[ATLAS_DB_NAME]
    yield
    # Shutdown logic
    app.mongodb_client.close