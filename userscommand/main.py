import uvicorn
from fastapi import FastAPI

from src.interfaces.api import user_controller
from src.interfaces.api.openapi import tags_metadata
from src.interfaces.api.exception_handlers import global_exception_handler

app = FastAPI(
    title="users-command",
    description="microservicio users command",
    version="0.0.1",
    openapi_tags=tags_metadata,
    )



# Registra el router de usuario
app.include_router(user_controller.router)

# Registrar el manejador de excepciones global
app.add_exception_handler(Exception, global_exception_handler)





if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)