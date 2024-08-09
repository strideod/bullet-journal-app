from fastapi import APIRouter, Depends

from api.v1 import entry_endpoints
from api.v1 import public_user_endpoints
from api.v1 import authenticated_user_endpoints
from core.dependencies import get_current_user

router = APIRouter()

router.include_router(
    public_user_endpoints.router,
    tags=["users"]
)

router.include_router(
    entry_endpoints.router,
    dependencies=[Depends(get_current_user)],
    tags=["entries"], 
    prefix="/entries")

router.include_router(
    authenticated_user_endpoints.router,
    tags=["users"],
)