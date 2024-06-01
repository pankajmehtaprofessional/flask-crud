from flask import Blueprint, jsonify, request
from src.controllers import UserController
from src.middlewares.custom import custom_middleware
from src.validations.user import GetUser
from src.lib import CustomError, Mail

user_bp = Blueprint("user", __name__)

@user_bp.get("/", endpoint="get_user")
@custom_middleware
def list_user():
    obj = UserController()
    data = obj.find()
    return data


@user_bp.post("/", endpoint="add_user")
@custom_middleware
def add():

    data = request.json

    obj = UserController()

    response = obj.add(data)

    return jsonify(str(response))


@user_bp.get("/<string:user_id>", endpoint="user_details")
@custom_middleware
def details(user_id):
    schema = GetUser()
    errors = schema.validate({"user_id": user_id})

    if errors:
        return jsonify(errors), 400
        
    obj = UserController()
    response = obj.details(user_id)
    return jsonify(response)


@user_bp.get("/count", endpoint="user_count")
@custom_middleware
def count():
    obj = UserController()

    response = obj.count()

    return str(response)


@user_bp.delete("/<string:_id>", endpoint="delete_user")
def delete(_id):
    obj = UserController()
    response = obj.delete(_id)
    return str(response)


@user_bp.get("/test", endpoint="test")
def test():
    raise CustomError("Here")

@user_bp.get("/mail", endpoint="mail")
def mail():
    hi = "test from here"
    mail_obj = Mail()
    mail_obj.send({
        "sender_email": "pankaj.mehta@appinventiv.com",
        "receiver_email": "pankaj.mehta@appinventiv.com",
        "subject": "Py Testing",
        "message": f"testing {str(hi)}"
    })
    return "Success Mail"
