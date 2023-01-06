from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange

class ServicesForm(FlaskForm):
    printfile = FileField('File', render_kw={"id": "print-id"}, validators=[DataRequired()])
    num_copies = IntegerField('Number of Copies', validators=[DataRequired(), NumberRange(min=1)])
    specification = TextAreaField('Specification', validators=[DataRequired()])
    submit = SubmitField('Submit Request')

    def render_field(self, field, render_kw):
        render_kw.update({"class": "form-modal-control"})
        return super().render_field(field, render_kw)