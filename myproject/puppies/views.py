from flask import Blueprint, render_template, redirect, url_for,session
from myproject import db
from myproject.puppies.forms import AddForm,DelForm
from myproject.models import Puppy

puppies_blueprint = Blueprint('puppies', __name__, template_folder="templates/puppies")

@puppies_blueprint.route("/add", methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        session["name"] = form.name.data

        new_pup = Puppy(session["name"])
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for("puppies.add_pup"))
    return render_template("add.html", form=form)

@puppies_blueprint.route("/list")
def list_pup():
    puppies = Puppy.query.all()
    return render_template("list.html", puppies=puppies)

@puppies_blueprint.route("/delete", methods=['GET', 'POST'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        session["id"] = form.id.data

        pup = db.session.get(Puppy, session["id"])
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for("puppies.list_pup"))
    return render_template("delete.html", form=form)