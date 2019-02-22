from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
