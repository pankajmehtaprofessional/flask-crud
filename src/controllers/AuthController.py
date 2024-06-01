from src.managers import UserManager

class AuthController:

    def __init__(self):
        self.USER_MANAGER = UserManager()

    def signup(self, params):

        isUserExist = self.USER_MANAGER.details()
        pass

    def login(self, params):
        pass

    def logout(self, params):
        pass
