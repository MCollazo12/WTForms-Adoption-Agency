from flask import Flask, redirect, render_template, request
from model import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey123"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template("/index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Displays a form for adding a new pet and handles form submission. """
    
    form = AddPetForm()
    
    if request.method == "POST" and form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
            available=form.available.data,
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("/add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def view_pet_details(pet_id):
    """ Displays details about a specific pet and handles editing of pet details."""
    
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if request.method == "POST" and form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        return redirect("/")
    return render_template("pet_detail.html", pet=pet, form=form)
