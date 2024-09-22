from abc import ABC, abstractmethod
from src.adapters.models.user_model import UserModel

class UserRepository(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> UserModel:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> UserModel:
        pass
    
    @abstractmethod
    def save(self, user_model: UserModel):
        pass
