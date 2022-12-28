from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, DateField
from wtforms.validators import DataRequired, InputRequired

class LoginForm(FlaskForm):
    username = StringField("Input username", validators=[DataRequired()])
    password = PasswordField(validators=[
        validators.DataRequired()
    ])
    submit = SubmitField("Login")


