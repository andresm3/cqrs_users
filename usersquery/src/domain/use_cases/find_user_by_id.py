
from src.domain.entities.user import User
from src.ports.repositories.user_repository import UserRepository


class FindUserByIdUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, id: int):
        return self.user_repository.find_by_id(id)