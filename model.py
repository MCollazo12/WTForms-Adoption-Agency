from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ Connects the database to the Flask app. """
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """
    Models pets potentially available for adoption.

    Attributes:
        id (int): The unique identifier for each pet.
        name (str): The name of the pet.
        species (str): The species of the pet.
        photo_url (str): The URL of the pet's photo.
        age (int): The age of the pet.
        notes (str): Any additional notes about the pet.
        available (bool): Indicates if the pet is available for adoption (default is true).
    """

    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=True, default=True)
