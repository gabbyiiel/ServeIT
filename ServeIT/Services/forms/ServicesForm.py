from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, TextAreaField, SubmitField, StringField, ValidationError, RadioField
from wtforms.validators import DataRequired, NumberRange, Regexp, InputRequired

def allowed_file_extensions(form, field):
        if not field.data:
            return
        # Get the file extension of the uploaded file
        file_extension = field.data.filename.rsplit('.', 1)[1].lower()

        # Set the allowed file extensions
        allowed_extensions = ['docx', 'pdf', 'pptx']
        # If the file extension is not in the allowed list, raise a ValidationError
        if file_extension not in allowed_extensions:
            raise ValidationError('Invalid file extension')


class PrintForm(FlaskForm):
    printfile = FileField('File', render_kw={"id": "print-id"}, validators=[DataRequired()])
    num_copies = IntegerField('Number of Copies', validators=[DataRequired(), NumberRange(min=1)])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit Request')
    

class GcashForm(FlaskForm):
    phone_number = StringField('Phone Number', validators=[DataRequired(), Regexp(r'^\+?1?\d{9,14}$', message="Phone number must be in the format: '+999999999'"), Regexp(r'^[0-9]*$', message="Phone number can only contain digits.")])
    amount = IntegerField('Amount', validators=[DataRequired(), NumberRange(min=20, max=5000)])
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Submit Request')

    

