from datetime import datetime
import json
from flask import Flask
from dotenv import load_dotenv
from bson.objectid import ObjectId
from src import Bootstrap
from src.middlewares import before_request

load_dotenv()

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)

app.json_encoder = CustomJSONEncoder

""" 
Before request middleware
"""
@app.before_request
def before_request_wrapper():
    before_request()

Bootstrap.init(app)

if __name__ == '__main__':
    app.run(debug = True)
