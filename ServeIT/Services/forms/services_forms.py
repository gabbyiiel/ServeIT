from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class PrintForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    num_copies = IntegerField('Number of Copies', validators=[DataRequired(), NumberRange(min=1)])
    specification = TextAreaField('Specification', validators=[DataRequired()])
