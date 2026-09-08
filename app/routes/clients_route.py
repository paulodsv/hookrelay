from fastapi import APIRouter, Depends
from app.schemas.clients import CreateClient
from app.core.deps import get_db, get_client_service
from app.service.clients import ClientService

clients_router = APIRouter(prefix="/clients", tags=["Clients"])

@clients_router.post("/")
async def create_client(client_data: CreateClient, service = Depends(get_client_service)):
    return await service.create_client_service(client_data)