
class CreateUserCommand:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
