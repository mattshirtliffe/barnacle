from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LeadForm(FlaskForm):
    # name = StringField('name', [DataRequired()])
    first_name = StringField('first_name', [DataRequired()])
    last_name = StringField('last_name', [DataRequired()])
    # company_name = StringField('company_name', [DataRequired()])
    email = EmailField('email', [DataRequired()])
    phone = StringField('phone')
    # has_accepted_terms = BooleanField('accepted_terms', [DataRequired()])
