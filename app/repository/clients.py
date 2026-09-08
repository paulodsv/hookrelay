from app.schemas.clients import CreateClient

class ClientRepository():
    def __init__(self, db):
        self.db = db

    async def save_client(self, client_data: CreateClient):
        client_id = await self.db.fetchrow("INSERT INTO clients(name) VALUES($1) RETURNING id, name, ingest_key, created_at", client_data.name)
        return client_id