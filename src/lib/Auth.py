import bcrypt
import os
import jwt

class Auth:

    ALGORITHM="HS356"
    SECRET_KEY=os.getenv("SECRET_KEY")

    def __init__(self):
        self.salt = bcrypt.gensalt()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.salt)

    def compare_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def create_token(self, payload):
        return jwt.encode(payload, self.SECRET_KEY, self.ALGORITHM)

    def verify_token(self, token):
        try:
            return jwt.decode(token, self.SECRET_KEY, self.ALGORITHM)
        except jwt.ExpiredSignatureError:
            return "Token expired"
        except jwt.InvalidTokenError:
            return "Invalid token"
