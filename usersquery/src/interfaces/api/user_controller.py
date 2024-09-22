
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.domain.use_cases.find_user_by_id import FindUserByIdUseCase
from src.domain.use_cases.find_user_by_email import FindUserByEmailUseCase
from src.interfaces.config_db import SessionLocal
from src.interfaces.api.errors import ValidationError
from src.interfaces.redis_cache import redis_cache

router = APIRouter()


class UserRequest(BaseModel):
    email: str


@router.get("/users/{user_id}", tags=["users"], description="Find User by Id")
async def get_user_by_id(user_id: int) -> JSONResponse:

    session = SessionLocal()
    user_repo = SQLAlchemyUserRepository(session)
    use_case = FindUserByIdUseCase(user_repo, redis_cache)
    user = await use_case.execute(user_id)
    session.close()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", tags=["users"], description="Find User by email")
def get_user_by_email(request: UserRequest) -> JSONResponse:

    try:
        session = SessionLocal()
        user_repo = SQLAlchemyUserRepository(session)
        use_case = FindUserByEmailUseCase(user_repo)
        user = use_case.execute(request.email)
        return user
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()
