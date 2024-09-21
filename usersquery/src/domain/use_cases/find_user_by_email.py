
from src.domain.entities.user import User
from src.ports.repositories.user_repository import UserRepository

class FindUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str):
        return self.user_repository.find_by_email(email)