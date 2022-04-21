from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe


@app.route('/show/recipes')
def show_user():
    return render_template('index.html',  user = User.get_one({'id': session['uuid']}), recipes = Recipe.get_all())

@app.route('/view/recipe/<int:id>')
def render_view_instructions(id):
    return render_template('view_instructions.html',user = User.get_one({'id': session['uuid']}), recipes = Recipe.get_one({'id': id}))