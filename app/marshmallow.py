# schemas.py

from marshmallow import Schema, fields, validates, ValidationError
from models import Hero, Power

# Hero Schema


class HeroSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)

    # Validation for description field
    @validates("description")
    def validate_description(self, value):
        if len(value) < 20:
            raise ValidationError(
                "Description must be at least 20 characters long.")

# Power Schema


class PowerSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)

    # Validation for description field
    @validates("description")
    def validate_description(self, value):
        if len(value) < 20:
            raise ValidationError(
                "Description must be at least 20 characters long.")
