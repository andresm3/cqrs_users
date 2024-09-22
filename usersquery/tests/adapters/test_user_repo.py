import unittest
from unittest.mock import MagicMock, Mock
from src.adapters.repositories.user_repo import SQLAlchemyUserRepository
from src.adapters.models.user_model import UserModel

class TestSQLAlchemyUserRepository(unittest.TestCase):

    def setUp(self):
        # Crear un mock para la sesión de SQLAlchemy
        self.session_mock = MagicMock()

        # Instanciar el repositorio con el mock de la sesión
        self.user_repository = SQLAlchemyUserRepository(self.session_mock)

    def test_find_user(self):
        # Given
        user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.user_repository.save(user)

        # When
        self.user_repository.find_by_id(10)

        # Then
        self.session_mock.query.assert_called_once()
