import json
from flask import request

def before_request():
    print(
        "---------------------- Headers ----------------------\n",
        json.dumps(dict(request.headers), indent=4),
        "\n----------------------"
    )