from services.user_service import UserService
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import responses
from fastapi import status
from fastapi.templating import Jinja2Templates
from schemas.users im

router = APIRouter


@router.get("/register/")
def register(request: Request):
    return template.TemplateResponse("user/register.html", {"request": request})

