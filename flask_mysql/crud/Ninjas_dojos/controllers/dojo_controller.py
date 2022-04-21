from __init__ import app
from flask import render_template, request, redirect, session
from models.dojo import Dojo
from models.ninja import Ninja

@app.route('/dojos')
def display_dojos():
    return render_template('/index.html', dojos=Dojo.get_all())

@app.route('/dojos/<int:id>')
def display_dojo_stu(id):
    return render_template('/show.html', students=Ninja.get_dojoinfo({'id':id}), dojos=Dojo.getinfo({'id':id}))

@app.route('/create_dojo', methods=['post']) #make route /dojo/create
def new_dojo():
    Dojo.create(request.form)
    return redirect ('/dojos')