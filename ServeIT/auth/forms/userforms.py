from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, SelectField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField("Password",validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class SignupForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email',validators=[validators.Email()])
    idnumber = StringField('Id Number', [validators.Length(min=9, max=9), validators.Regexp(r'^\d{4}-\d{4}$', message='ID number must be in integer ex 2000-0001'), validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=8)])
    username = StringField('Username',validators=[validators.Length(min=4, max=25)])
    submit = SubmitField('Sign Up')
