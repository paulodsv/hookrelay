from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from app.database.connection import create_db_pool
from app.routes.users_route import users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await create_db_pool()

    yield

    await app.state.db.close()

app = FastAPI(title="HookRelay API", lifespan=lifespan)

@app.get("/health")
async def get_health(request: Request):

    db = request.app.state.db

    async with db.acquire() as conn:
        result = await conn.fetchval("SELECT 1")

    return {
        "status": "ok",
        "database": "ok" if result == 1 else "error"
    }

app.include_router(users_router)