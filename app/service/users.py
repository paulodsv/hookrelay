from app.repository.users import UserRepository
from fastapi import HTTPException, status
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.users import CreateUser, UserLogin, TokenResponse

class UserService():
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user_service(self, user_data: CreateUser):
        hashed_pass = hash_password(user_data.password)
        user_data.password = hashed_pass

        try:
            return await self.user_repo.save_user(user_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro interno ao salvar usuário. Erro: {e}")

    async def user_login_service(self, user_login_data: UserLogin) -> TokenResponse:
        user = await self.user_repo.get_user_by_email(user_login_data.email)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        if not verify_password(user_login_data.password, user["password_hash"]):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

        return TokenResponse(access_token=create_access_token(user["id"]))