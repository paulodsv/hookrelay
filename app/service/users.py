from app.repository.users import UserRepository
from fastapi import HTTPException
from app.core.security import hash_password
from app.schemas.users import CreateUser

class UserService():
    def __init__(self, db, user_repo: UserRepository):
        self.db = db
        self.user_repo = user_repo

    async def create_user_service(self, user_data: CreateUser):
        hashed_pass = hash_password(user_data.password)
        user_data.password = hashed_pass
        
        try:
            return await self.user_repo.save_user(user_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro interno ao salvar usuário. Erro: {e}")