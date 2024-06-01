from src.lib.Auth import Auth
from src.lib.Exception import CustomError
from src.controllers.UserController import UserController

class AuthController:

    def __init__(self):
        self.auth = Auth()
        self.user_controller = UserController()

    def login(self, params=None):
        
        try:

            raise CustomError("")

            # details = self.user_controller.details(params["user_id"])

            # if details:
                # raise CustomError("")

            # response = self.auth.compare_password("12345678", params["password"])

            return 1
        except:
            print("Error")
            raise

    def register(self, params):

        try:
            response = self.auth.hash_password(params["password"])
            return response
        except:
            print("Error")
            raise

    def reset_password(self):
        return

    def resend_verification_link(self):
        return
