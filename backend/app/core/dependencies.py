from typing import Annotated

from fastapi import Depends, HTTPException, status

from core.security import oauth2_scheme


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO logic to get current user
    # For demonstraion, we will just return the token
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token