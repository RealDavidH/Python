from types import NoneType
from flask_app import app, DATABASE, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_user import User

@app.route('/')
def show_users():
    return render_template('index.html', users = User.get_all(), friends = User.get_friends())

@app.route('/create/user', methods=['post'])
def create_user():
    User.create(request.form)
    return redirect('/')

@app.route('/add/friend', methods=['post'])
def add_friend():
    if not User.validate(request.form):
        return redirect('/')
    User.add_friend(request.form)
    return redirect('/')
