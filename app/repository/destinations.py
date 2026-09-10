from app.schemas.destinations import CreateDestination

class DestinationsRepository():
    def __init__(self, db):
        self.db = db

    async def save_destination(self, user_id: int, destination_data: CreateDestination):
        return await self.db.fetchrow("INSERT INTO destinations (user_id, name, url) VALUES ($1, $2, $3) RETURNING *", user_id, destination_data.name, destination_data.url)