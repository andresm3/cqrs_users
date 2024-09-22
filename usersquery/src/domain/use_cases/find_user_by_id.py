
from src.ports.repositories.user_repository import UserRepository
from src.interfaces.redis_cache import redis_cache


class FindUserByIdUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int):
        cached_user = await redis_cache.get(f"user:{user_id}")
        print("************cached_user------- ", cached_user)
        if cached_user:
            return cached_user
        
        user = self.user_repository.find_by_id(user_id)
        print("************user------- ", user)
        if user:
            await redis_cache.set(f"user:{user_id}", user.to_dict())

        return user