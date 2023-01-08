from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FileField, validators, SelectField, RadioField
from wtforms.validators import DataRequired, Email

class AccountForm(FlaskForm):
    fname = StringField("First Name", validators=[DataRequired()])
    lname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    idnumber = StringField('Id Number')
    college = SelectField('College',choices=[('' , 'College'),('CCS' , 'CCS'),('CSM', 'CSM'),('CEBA', 'CEBA'),('CASS', 'CASS'),('CON', 'CON'),('CED', 'CED'),('COET', 'COET')],)
    course = SelectField('Course', choices=[('','Course')])
    username = StringField('Username',validators=[validators.Length(min=4, max=25)])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')], render_kw={'class': 'form-check-input'}) 
    password = PasswordField('Password', validators=[validators.Length(min=8)])
    submit = SubmitField("Update")
    imgFile = FileField('Photo', validators=[FileAllowed('image')])
    submit = SubmitField("Update")