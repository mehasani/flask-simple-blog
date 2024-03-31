from flask_wtf import FlaskForm
from wtforms import StringField, EmailField


class AdministratorLoginForm(FlaskForm):
    email = EmailField('Email')
    password = StringField('Password')
