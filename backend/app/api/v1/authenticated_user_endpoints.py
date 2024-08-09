from fastapi import APIRouter, Body, HTTPException, Request, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.users import User
from core.security import verify_password

router = APIRouter()

@router.post("/api/v1/login", response_description="Login to the applicaition", status_code=status.HTTP_202_ACCEPTED, response_model=User)
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user = request.app.database["users"].find_one({"username": form_data.username})

    if user and verify_password(user["password"], form_data.password):
        return user
    
    raise HTTPException(status_c0de=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
