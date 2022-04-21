from __init__ import app
from flask import render_template, request, redirect, session
from models.ninja import Ninja
from models.dojo import Dojo

@app.route('/ninjas')
def create_ninja():
    return render_template('create.html', dojos=Dojo.get_all())

@app.route('/create_ninja', methods=['post'])
def new_ninja():
    Ninja.create(request.form)
    return redirect('/dojos')