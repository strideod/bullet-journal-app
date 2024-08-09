from fastapi import APIRouter, Body, Request, status, HTTPException
from fastapi.encoders import jsonable_encoder

from models.users import User
from core.security import hash_password

router = APIRouter()

@router.post("/api/v1/signup", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def signup(request: Request, user: User = Body(...)):
    existing_user = request.app.database["users"].find_one({"username": user.username})
    if existing_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with username {user.username} already exists.")
    
    existing_email = request.app.database["users"].find_one({"email": user.email})
    if existing_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email {user.email} already exists.")
    
    hashed_password = hash_password(user.password)
    user = jsonable_encoder(user)
    user["password"] = hashed_password
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )

    return created_user
