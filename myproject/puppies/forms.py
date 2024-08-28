from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('Remove Puppy')