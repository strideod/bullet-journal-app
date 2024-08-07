from fastapi import APIRouter

from api.v1 import endpoints

router = APIRouter()
router.include_router(endpoints.router, tags=["entries"], prefix="/entries")