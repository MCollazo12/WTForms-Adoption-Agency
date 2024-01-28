from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    TextAreaField,
    BooleanField,
    ValidationError,
)
from wtforms.validators import InputRequired, Length, URL, Optional, AnyOf, NumberRange


class AddPetForm(FlaskForm):
    """
    Form for adding a new pet.

    Fields:
    - name: Pet's name (required)
    - species: Species of the pet (required)
    - photo_url: URL of the pet's photo (optional)
    - age: Age of the pet (optional)
    - notes: Additional notes about the pet (optional)
    - available: Availability status of the pet (required, defaults to available)
    """

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"])])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")
    available = BooleanField("Available for adoption?", default=True)

    def validate_species(form, field):
        """
        Validate's form input to ensure species is one of: cat, dog, or porcupine.
        Converts the user's species input to lowercase for case-insensitive matching.
        """

        species_lower = field.data.lower()
        valid_species = ["cat", "dog", "porcupine"]

        if species_lower not in valid_species:
            raise ValidationError()


class EditPetForm(FlaskForm):
    """
    Form for editing an existing pet's details.

    Fields:
    - photo_url: URL of the pet's photo (optional)
    - notes: Additional notes about the pet (optional)
    - available: Updated availability status of the pet (optional)
    """

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes")
    available = BooleanField("Available for adoption?")
