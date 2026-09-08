from asyncpg import UniqueViolationError
from app.repository.clients import ClientRepository
from fastapi import HTTPException

class ClientService():
    def __init__(self, db, client_repo: ClientRepository):
        self.db = db
        self.client_repo = client_repo

    async def create_client_service(self, client_data):
        try:
            return await self.client_repo.save_client(client_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro interno ao salvar usuário. Erro: {e}")