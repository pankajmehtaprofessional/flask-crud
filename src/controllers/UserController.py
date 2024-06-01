import datetime
from flask import jsonify
import bcrypt
from src.managers.UserManager import UserManager
from src.lib.Auth import Auth

class UserController:

    def __init__(self):
        self.manager = UserManager()
        self.auth = Auth()

    def details(self, user_id):
        response = dict(self.manager.find_one({ "_id": user_id }));

        result = self.auth.compare_password("12345678", response["password"])

        if result:
            print('Login successful')
            response["_id"] = str(response["_id"])
            response["password"] = str(response["password"])
        else:
            response = 'Login failed'

        return response

    def find(self):

        try:
            response = self.manager.find();
            print("------------------1-----------", response)
            for d in response:
                d["_id"] = str(d["_id"]);

            return jsonify(response);
        except Exception as e:
            print("Controller error", e);
            raise;

    def add(self, data):

        try:

            data["createdAt"] = datetime.datetime.now();
            data["updatedAt"] = datetime.datetime.now();

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), salt)

            data["password"] = hashed_password

            response = self.manager.insert_one(data).inserted_id;

            return response
        except:
            print("")
            raise;

    def count(self):
        try:
            response = self.manager.count();
            return response;
        except:
            print("")
            raise;

    def delete(self, _id):
        try:
            response = self.manager.delete(_id)
            return response.deleted_count
        except:
            print("")
            raise
        