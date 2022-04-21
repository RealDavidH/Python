from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_sighting import Sighting
from flask_app.models.model_skeptic import Skeptic


@app.route('/show/sightings')
def show_user():
    sightings = Sighting.join_sightings_one()
    print(sightings)
    return render_template('index.html',  user = User.get_one({'id': session['uuid']}),  sightings = sightings) 

@app.route('/view/sighting/<int:id>')
def render_view_sightings(id):
    sightings = Sighting.join_sightings_one({"id": id})
    print(sightings)
    return render_template('view_sighting.html', user = User.get_one({'id': session['uuid']}), sightings = sightings, skeptics = Skeptic.get_skep_name({"id": id}))