from flask import Flask, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

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


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, 
                  species=species, 
                  photo_url=photo_url, 
                  age=age, 
                  notes=notes)
        db.session.add(pet)
        db.session.commit()
       
        return redirect('/')

    else:
        return render_template(
            "add_pet_form.html", form=form)