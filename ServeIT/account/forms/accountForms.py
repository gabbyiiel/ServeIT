from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FileField, validators, SelectField, RadioField
from wtforms.validators import DataRequired, Email, Regexp, ValidationError

class SchoolInfoForm(FlaskForm):
    idnumber = StringField('Id Number', [validators.Length(min=9, max=9), validators.Regexp(r'^\d{4}-\d{4}$', message='ID number must be in integer ex 2000-0001'), validators.DataRequired()])
    submit = SubmitField("Update")

class BasicInfoForm(FlaskForm):
    fname = StringField("First Name", validators=[DataRequired()])
    lname = StringField("Last Name", validators=[DataRequired()])
    contactnum = StringField('Contact Number', validators=[DataRequired(), Regexp(r'^\+?1?\d{9,14}$', message="Phone number must be in the format: '+999999999'"), Regexp(r'^[0-9]*$', message="Phone number can only contain digits.")])
    submit = SubmitField("Update")

class UserInfoForm(FlaskForm):
    username = StringField('Username',validators=[validators.Length(min=4, max=25)])
    password = PasswordField('Password', validators=[validators.Length(min=8)])
    verify_password = PasswordField('Verify Password')
    submit = SubmitField("Update")

    def validate_verify_password(self, field):
        if field.data != self.password.data:
            raise ValidationError('Passwords do not match')

