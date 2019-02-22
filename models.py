from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """Defines class of pets. It is the pets table in the database"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                   nullable=False)
    species = db.Column(db.String(50),
                   nullable=True)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer,
                    nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                    nullable=False,
                    default=True)


def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)