from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from argon2 import PasswordHasher, exceptions, Type

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_password_request_form = OAuth2PasswordRequestForm


def hash_password(password: str) -> str:
    ph = PasswordHasher(type=Type.ID)
    return ph.hash(password)

def verify_password(hashed_password: str, plain_password) -> bool:
    try:
        return PasswordHasher().verify(hashed_password, plain_password)
    except exceptions.VerifyMismatchError:
        return False