from fastapi import Request, Depends
from app.repository.users import UserRepository
from app.service.users import UserService

async def get_db(request: Request):
    async with request.app.state.db.acquire() as conn:
        yield conn

async def get_user_service(db = Depends(get_db)):
    user_repo = UserRepository(db)
    service = UserService(db, user_repo)
    return service