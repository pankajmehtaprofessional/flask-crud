import dataclasses
from marshmallow import Schema, fields, EXCLUDE

class GetUser(Schema):
    
    @dataclasses.dataclass
    class Meta:
        unknown = EXCLUDE

    user_id = fields.Str(
        required=True,
        error_messages={
            "required": "Field required",
        }
    )

class AddUser(Schema):

    @dataclasses.dataclass
    class Meta:
        unknown = EXCLUDE

    email = fields.Str(
        required=True,
        error_messages= {
            "required": "Required"
        }
    )
    password = fields.Str(
        required=True,
        error_messages= {
            "required": "Required"
        }
    )
    lname = fields.Str(
        required=True,
        error_messages= {
            "required": "Required"
        }
    )
    fname = fields.Str(
        required=True,
        error_messages= {
            "required": "Required"
        }
    )
    