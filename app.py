from flask import Flask, render_template, redirect, flash, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SECRET_KEY'] = "cheese_sombreros"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def show_homepage():
    """ Shows homepage with list of available pets. """

    pets = Pet.query.all()

    return render_template('homepage.html', pets=pets)