from fastapi import APIRouter, Depends
from app.schemas.destinations import CreateDestination
from app.core.deps import get_destination_service, get_current_user
from app.service.destinations import DestinationsService

destination_router = APIRouter(prefix="/destinations", tags=["Destinations"])

@destination_router.post("/")
async def create_destination(destination_data: CreateDestination, 
                             service: DestinationsService = Depends(get_destination_service), 
                             current_user: int =  Depends(get_current_user)):
    return await service.create_destination_service(user_id=current_user["id"], destination_data=destination_data)