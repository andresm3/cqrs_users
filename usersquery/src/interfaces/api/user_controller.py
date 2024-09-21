
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.domain.use_cases.find_user_by_id import FindUserByIdUseCase
from src.interfaces.config_db import SessionLocal
from src.interfaces.redis_cache import redis_cache

router = APIRouter()


@router.get("/users/{user_id}")
async def get_user(user_id: int):

    cached_user = await redis_cache.get(f"user:{user_id}")
    print("************cached_user------- ", cached_user)
    if cached_user:
        return cached_user
    
    session = SessionLocal()
    user_repo = SQLAlchemyUserRepository(session)
    use_case = FindUserByIdUseCase(user_repo)
    user = await use_case.execute(user_id)
    print("************user------- ", user)
    session.close()

    if user:
        await redis_cache.set(f"user:{user_id}", user)
    else:
        raise HTTPException(status_code=404, detail="User not found")
    return user