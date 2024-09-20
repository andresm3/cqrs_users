
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.is_active = False

    def activate(self):
        self.is_active = True
