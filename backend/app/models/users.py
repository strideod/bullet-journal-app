from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    password: 
    disabled: bool | None = None