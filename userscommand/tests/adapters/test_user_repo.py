import unittest
from unittest.mock import MagicMock, Mock
from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.domain.entities.user import User
from src.adapters.models.user_model import UserModel

class TestSQLAlchemyUserRepository(unittest.TestCase):

    def setUp(self):
        # Crear un mock para la sesión de SQLAlchemy
        self.session_mock = MagicMock()

        # Instanciar el repositorio con el mock de la sesión
        self.user_repository = SQLAlchemyUserRepository(self.session_mock)

    def test_save_user(self):
        # Given
        user = User(username="testuser", email="test@example.com", password="123123")

        # When
        self.user_repository.save(user)

        # Then
        self.session_mock.add.assert_called_once()
        self.session_mock.commit.assert_called_once()
