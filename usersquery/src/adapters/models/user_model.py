from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from src.domain.entities.user import User as DomainUser

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
        }

    def to_domain(self) -> DomainUser:
        """
        Convierte el modelo SQLAlchemy a una entidad del dominio.
        """
        user = DomainUser(self.username, self.email, self.password)
        return user

    @classmethod
    def from_domain(cls, user: DomainUser):
        """
        Convierte una entidad de dominio a un modelo SQLAlchemy.
        """
        return cls(username=user.username, email=user.email, password=user.password, is_active=user.is_active)
