from flask import Flask, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetPage
from secrets import PETFINDER_API_KEY
from petfinder_API import get_info_random_pet
import requests

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
    rando_pet = get_info_random_pet()

    name = rando_pet['petfinder']['pet']['name']['$t']
    age = rando_pet['petfinder']['pet']['age']['$t']
    image = rando_pet['petfinder']['pet']['media']['photos']['photo'][0]['$t']

    return render_template('homepage.html', pets=pets,
                            name=name, age=age, image=image)


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


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_and_edit_pet_page(pet_id):
    """ Shows individual pet page. """
   
    pet = Pet.query.get(pet_id)

    form = EditPetPage(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect('/')

    else:
        return render_template('display_pet.html', pet=pet, form=form)