from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, SelectField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField("Password",validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

class SignupForm(FlaskForm):
    fname = StringField('First Name')
    lname = StringField('Last Name')
    email = StringField('Email',validators=[validators.Email()])
    idnumber = StringField('Id Number')
    
    college = SelectField('College',choices=[('' , 'College'),('CCS' , 'CCS'),('CSM', 'CSM'),('CEBA', 'CEBA'),('CASS', 'CASS'),('CON', 'CON'),('CED', 'CED'),('COET', 'COET')],)
    
    course = SelectField('Course', choices=[('','Course')])
    password = PasswordField('Password', validators=[
        validators.Length(min=8)])
    username = StringField('Username',validators=[validators.Length(min=4, max=25)])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], render_kw={'class': 'form-check-input'}) 
    submit = SubmitField('Sign Up')
