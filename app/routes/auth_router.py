from fastapi import APIRouter, Depends
from app.schemas.users import UserLogin
from app.core.deps import get_user_service
from app.service.users import UserService

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/")
async def login(user_login_data: UserLogin, service: UserService = Depends(get_user_service)):
    return await service.user_login_service(user_login_data)