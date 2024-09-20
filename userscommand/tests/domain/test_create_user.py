import unittest
from unittest.mock import Mock
from src.domain.use_cases.create_user import CreateUserUseCase
from src.interfaces.api.errors import ValidationError

class TestCreateUserUseCase(unittest.TestCase):
    def test_create_user(self):
        # Crear un mock para el repositorio
        mock_repo = Mock()
        
        # Instanciar el caso de uso con el mock
        create_user_use_case = CreateUserUseCase(mock_repo)
        
        # Ejecutar el caso de uso
        create_user_use_case.execute("test_user", "test@example.com", "123456")
        
        # Verificar que el método save del repositorio fue llamado
        mock_repo.save.assert_called_once()

    def test_create_user_with_invalid_email(self):
        # Crear un mock del repositorio
        mock_repo = Mock()

        # Instanciar el caso de uso
        create_user_use_case = CreateUserUseCase(mock_repo)

        # Verificar que la excepción se lanza cuando el email es inválido
        with self.assertRaises(ValidationError):
            create_user_use_case.execute("username", "invalid-email", "123456")
