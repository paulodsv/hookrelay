from app.schemas.users import CreateUser

class UserRepository():
    def __init__(self, db):
        self.db = db

    async def save_user(self, user_data: CreateUser):
        user = await self.db.fetchrow("INSERT INTO users(name, email, password_hash) VALUES($1, $2, $3) RETURNING id, name, email, ingest_key, created_at", user_data.name, user_data.email, user_data.password)
        return user