from sqlalchemy.orm import Session
from src.ports.repositories.user_repository import UserRepository
from src.domain.entities.user import User
from src.adapters.models.user_model import UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: User):
        user_model = UserModel.from_domain(user)  # Convierte de entidad de dominio a modelo SQLAlchemy
        self.session.add(user_model)
        self.session.commit()
