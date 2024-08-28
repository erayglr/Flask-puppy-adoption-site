from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddOwner(FlaskForm):
    name = StringField('Name of Owner:', validators=[DataRequired()])
    id = IntegerField('Id of Puppy:', validators=[DataRequired()])
    submit = SubmitField('Add Owner')