from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm) :
    def __init__(self) :
        self.name = String('name',validators=[DataRequired])
        self.email = ""
        self.subject = ""
        self.message = ""