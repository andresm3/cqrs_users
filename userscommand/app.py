import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.domain.use_cases.create_user import CreateUserUseCase
from src.interfaces.api.openapi import tags_metadata
from src.interfaces.config_db import SessionLocal
from src.interfaces.api.errors import ValidationError
from src.interfaces.api.exception_handlers import global_exception_handler

app = FastAPI(
    title="ms-users-command",
    description="microservicio users command",
    version="0.0.1",
    openapi_tags=tags_metadata,
)


class RegisterUserRequest(BaseModel):
    username: str
    email: str
    password: str

@app.post("/users/register", tags=["users"], description="Create a new user")
def create_user(request: RegisterUserRequest) -> JSONResponse:
    session = SessionLocal()
    try:
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

# Registrar el manejador de excepciones global
app.add_exception_handler(Exception, global_exception_handler)

if __name__ == '__main__':
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)