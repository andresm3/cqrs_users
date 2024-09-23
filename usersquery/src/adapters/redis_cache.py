from redis import asyncio as aioredis # a partir de python 3.11, usar esta lib
import json

from src.ports.repositories.cache_repository import CacheRepository

class RedisCache(CacheRepository):
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url('redis://localhost')

    async def get(self, key):
        value = await self.redis.get(key)
        if value:
            return json.loads(value)
        return None

    async def set(self, key, value):
        await self.redis.set(key, json.dumps(value))

    async def close(self):
        self.redis.close()
        await self.redis.wait_closed()

# Instancia global de RedisCache
redis_cache = RedisCache()

# Llamamos a connect en el arranque de la app
async def init_redis():
    await redis_cache.connect()
