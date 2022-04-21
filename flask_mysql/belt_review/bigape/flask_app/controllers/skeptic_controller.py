from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_skeptic import Skeptic

@app.route('/create/skeptic/<int:user_id>/<int:sightings_id>')
def add_skeptic(user_id, sightings_id):
    Skeptic.create({'users_id': user_id, 'sightings_id': sightings_id})
    return redirect(f'/view/sighting/{sightings_id}')

@app.route('/delete/skeptic/<int:user_id>/<int:sightings_id>')
def delete_skeptic(user_id, sightings_id):
    Skeptic.delete_one({'user_id':user_id})
    return redirect(f'/view/sighting/{sightings_id}')