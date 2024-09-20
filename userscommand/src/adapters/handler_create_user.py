

from src.domain.use_cases.create_user import CreateUserUseCase
from src.adapters.command_create_user import CreateUserCommand
from src.ports.repositories.user_repository import UserRepository
from src.adapters.command_create_user import CreateUserCommand

class CreateUserHandler:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self, command: CreateUserCommand):
        """
        Ejecuta el caso de uso utilizando el comando proporcionado.
        """
        use_case = CreateUserUseCase(self.user_repository)
        use_case.execute(command.username, command.email, command.password)
