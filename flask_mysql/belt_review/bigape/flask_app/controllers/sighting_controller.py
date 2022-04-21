from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_sighting import Sighting
from flask_app.models.model_user import User

@app.route('/sighting/new')
def render_create_sighting():
    return render_template('create_sighting.html', user = User.get_one({'id': session['uuid']}))

@app.route('/create/sighting', methods = ['post'])
def create_sighting():
    if not Sighting.validate(request.form):
        return redirect('/sighting/new')
    data= {
        **request.form,
        'user_id' : session['uuid']
    }
    Sighting.create(data)
    return redirect('/show/sightings')

@app.route('/delete/sighting/<int:id>')
def delete_sighting(id):
    Sighting.delete_one({'id': id})
    return redirect('/show/sightings')

@app.route('/edit/sighting/<int:id>')
def render_edit_sighting(id):
    return render_template('edit_sighting.html', sightings = Sighting.get_one({'id': id}), user = User.get_one({'id': session['uuid']}))

@app.route('/update/sighting', methods=['post'])
def edit_sighting():
    if not Sighting.validate(request.form):
        return redirect(f"/edit/sighting/{request.form['id']}")
    Sighting.update_one(request.form)
    return redirect ('/show/sightings')

