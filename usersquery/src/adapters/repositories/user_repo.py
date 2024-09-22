from sqlalchemy.orm import Session
from src.ports.repositories.user_repository import UserRepository
from src.domain.entities.user import User
from src.adapters.models.user_model import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_by_email(self, email: str) -> UserModel:
        user_model = self.session.query(UserModel).filter_by(email=email).first()
        if user_model:
            return user_model
        return None

    def find_by_id(self, id: int) -> UserModel:
        user_model = self.session.query(UserModel).filter(UserModel.id == id).first()
        if user_model:
            return user_model
        return None
    
    def save(self, user_model: UserModel):
        self.session.add(user_model)
        self.session.commit()