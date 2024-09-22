
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.domain.use_cases.create_user import CreateUserUseCase
from src.interfaces.config_db import SessionLocal
from src.interfaces.api.errors import ValidationError

router = APIRouter()

class RegisterUserRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/users/register", tags=["users"], description="Create a new user")
def create_user(request: RegisterUserRequest) -> JSONResponse:
    
    try:
        session = SessionLocal()
        user_repo = SQLAlchemyUserRepository(session)
        create_user_use_case = CreateUserUseCase(user_repo)
        create_user_use_case.execute(request.username, request.email, request.password)
        return JSONResponse(
            status_code=201,
            content={"message": "User created"}
        )
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        session.close()
