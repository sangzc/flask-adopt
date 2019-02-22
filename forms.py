from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name")
    species = StringField("Species",
                          validators=[AnyOf(('cat', 'dog', 'porcupine'),
                          message='pick either cat, dog, or porcupine')])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")
