from flask import Blueprint, render_template, redirect, url_for, session
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddOwner

owners_blueprints = Blueprint("owners",__name__,
                              template_folder="templates/owners")

@owners_blueprints.route("/add", methods=["GET", "POST"])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        session["name"] = form.name.data
        session["id"] = form.id.data
        new_owner = Owner(session["name"], session["id"])
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for("owners.add_owner"))
    return render_template("add_owner.html", form=form)