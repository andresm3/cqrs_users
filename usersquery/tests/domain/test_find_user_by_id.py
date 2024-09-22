import unittest
from unittest.mock import Mock
from src.domain.use_cases.find_user_by_id import FindUserByIdUseCase
from src.adapters.models.user_model import UserModel

class TestFindUserByIdUseCase(unittest.TestCase):

    def setUp(self):
        # Crear el mock del repositorio
        self.mock_user_repository = Mock()

        # Crear el servicio con el repositorio mockeado
        self.use_case = FindUserByIdUseCase(self.mock_user_repository)

    async def test_find_user_by_id_RepoOK(self):
        # Given
        existing_user = UserModel(id=10, username="testuser", email="test@example.com", password="123123")
        self.mock_user_repository.find_by_id.return_value = existing_user
        self.mock_user_repository.find_by_id.return_value = existing_user
        
        # When
        result = self.use_case.execute(10)
        
        # Then
        self.assertEqual(result, existing_user)
        self.mock_user_repository.find_by_id.assert_called_once_with(10)


