from email_validator import EmailNotValidError, validate_email

from src.domain.entities.user import User
from src.ports.repositories.user_repository import UserRepository
from src.interfaces.api.errors import ValidationError

class FindUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str):
        try:
            validated_email = validate_email(email, check_deliverability=False)
            return self.user_repository.find_by_email(validated_email.normalized)
        except EmailNotValidError as error:
            raise ValidationError(f"Provided email value `{email}` is not correct") from error
