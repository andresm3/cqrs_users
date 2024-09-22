from email_validator import EmailNotValidError, validate_email

from src.domain.entities.user import User
from src.ports.repositories.user_repository import UserRepository
from src.interfaces.api.errors import ValidationError

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, username: str, email: str, password: str):
        try:
            validated_email = validate_email(email, check_deliverability=False)
            user = User(username, validated_email.normalized, password)
            user.activate()
            self.user_repository.save(user)
        except EmailNotValidError as error:
            raise ValidationError(f"Provided email value `{email}` is not correct") from error
