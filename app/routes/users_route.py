from fastapi import APIRouter, Depends
from app.schemas.users import CreateUser
from app.core.deps import get_user_service
from app.service.users import UserService

users_router = APIRouter(prefix="/clients", tags=["Clients"])

@users_router.post("/")
async def create_user(user_data: CreateUser, service: UserService = Depends(get_user_service)):
    return await service.create_user_service(user_data)