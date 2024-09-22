import unittest
from unittest.mock import Mock
from src.domain.use_cases.find_user_by_email import FindUserByEmailUseCase
from src.interfaces.api.errors import ValidationError
from src.adapters.models.user_model import UserModel

class TestFindUserByEmailUseCase(unittest.TestCase):

    def setUp(self):
        # Crear el mock del repositorio
        self.mock_user_repository = Mock()

        # Crear el servicio con el repositorio mockeado
        self.use_case = FindUserByEmailUseCase(self.mock_user_repository)

    def test_find_user_by_email_OK(self):
        # Given
        existing_user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.mock_user_repository.find_by_email.return_value = existing_user
        
        # When
        result = self.use_case.execute('test@example.com')
        
        # Then
        self.assertEqual(result, existing_user)
        self.mock_user_repository.find_by_email.assert_called_once_with("test@example.com")

    def test_find_user_by_email_None(self):
        # Given
        existing_user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.mock_user_repository.find_by_email.return_value = existing_user
        
        # When
        result = self.use_case.execute('lolo@example.com')
        
        # Then
        self.mock_user_repository.find_by_email.assert_called_once_with("lolo@example.com")

    def test_find_user_with_invalid_email(self):

        # When Then
        with self.assertRaises(ValidationError):
            self.use_case.execute("invalid-email")
