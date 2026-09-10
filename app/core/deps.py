from fastapi import Request, Depends
from app.repository.users import UserRepository
from app.repository.destinations import DestinationsRepository
from app.service.users import UserService
from app.service.destinations import DestinationsService
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_access_token

async def get_db(request: Request):
    async with request.app.state.db.acquire() as conn:
        yield conn

async def get_user_service(db = Depends(get_db)):
    user_repo = UserRepository(db)
    service = UserService(user_repo)
    return service

async def get_destination_service(db = Depends(get_db)):
    destination_repo = DestinationsRepository(db)
    service = DestinationsService(destination_repo)
    return service



bearer_scheme = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), 
    db = Depends(get_db)
):
    token = credentials.credentials
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