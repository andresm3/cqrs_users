import uvicorn
from fastapi import FastAPI

from src.interfaces.api import user_controller
from src.interfaces.api.openapi import tags_metadata
from src.adapters.redis_cache import init_redis

app = FastAPI(
    title="users-query",
    description="microservicio users query",
    version="0.0.1",
    openapi_tags=tags_metadata,
    )


@app.on_event("startup")
async def startup_event():
    await init_redis()

# Registra el router de usuario
app.include_router(user_controller.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8010, reload=True)