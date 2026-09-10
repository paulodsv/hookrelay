from app.repository.destinations import DestinationsRepository
from app.schemas.destinations import CreateDestination

class DestinationsService():
    def __init__(self, dest_repo: DestinationsRepository):
        self.dest_repo = dest_repo

    async def create_destination_service(self, user_id: int, destination_data: CreateDestination):
        return await self.dest_repo.save_destination(user_id, destination_data)