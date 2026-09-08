from fastapi import Request, Depends
from app.repository.clients import ClientRepository
from app.service.clients import ClientService

async def get_db(request: Request):
    async with request.app.state.db.acquire() as conn:
        yield conn

async def get_client_service(db = Depends(get_db)):
    client_repo = ClientRepository(db)
    service = ClientService(db, client_repo)
    return service