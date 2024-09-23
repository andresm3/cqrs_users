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

    def test_find_user_OK(self):
        # Given
        expected_user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.session_mock.query().filter().first.return_value = expected_user

        # When
        result = self.user_repository.find_by_id(10)

        # Then
        self.assertEqual(result, expected_user)

    def test_find_user_by_email_OK(self):
        # Given
        expected_user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.session_mock.query().filter_by().first.return_value = expected_user

        # When
        result = self.user_repository.find_by_email("test@example.com")

        # Then
        self.assertEqual(result, expected_user)

