
from src.ports.repositories.user_repository import UserRepository
from src.ports.repositories.cache_repository import CacheRepository


class FindUserByIdUseCase:
    def __init__(self, user_repository: UserRepository, redis_cache:CacheRepository):
        self.user_repository = user_repository
        self.redis_cache = redis_cache

    async def execute(self, user_id: int):
        cached_user = await self.redis_cache.get(f"user:{user_id}")
        print("************cached_user------- ", cached_user)
        if cached_user:
            return cached_user
        
        user = self.user_repository.find_by_id(user_id)
        print("************user------- ", user)
        if user:
            await self.redis_cache.set(f"user:{user_id}", user.to_dict())

        return user