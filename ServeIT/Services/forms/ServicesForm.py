from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, TextAreaField, SubmitField, StringField, ValidationError, RadioField
from wtforms.validators import DataRequired, NumberRange

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


class ServicesForm(FlaskForm):
    printfile = FileField('File', render_kw={"id": "print-id"}, validators=[DataRequired()])
    num_copies = IntegerField('Number of Copies', validators=[DataRequired(), NumberRange(min=1)])
    specification = TextAreaField('Specification', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

    
    submit = SubmitField('Submit Request')

    

