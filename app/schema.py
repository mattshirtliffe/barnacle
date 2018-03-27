
from marshmallow import Schema, fields


class LeadSchema(Schema):
    email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    has_accepted_terms = fields.Bool()
    company_name = fields.Str()

    date_created = fields.Date()
    date_modified = fields.Date()
