from fastapi import Request, Depends
from app.repository.users import UserRepository
from app.service.users import UserService
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_access_token

async def get_db(request: Request):
    async with request.app.state.db.acquire() as conn:
        yield conn

async def get_user_service(db = Depends(get_db)):
    user_repo = UserRepository(db)
    service = UserService(db, user_repo)
    return service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme), db = Depends(get_db)):
    payload = decode_access_token(token)

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    repo = UserRepository(db)
    user = await repo.get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return user