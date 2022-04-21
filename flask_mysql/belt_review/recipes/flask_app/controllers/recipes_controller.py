from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User

@app.route('/recipes/new')
def render_create_recipe():
    return render_template('create_recipe.html')

@app.route('/create/recipe', methods = ['post'])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect('/recipes/new')
    data= {
        **request.form,
        'user_id' : session['uuid']
    }
    Recipe.create(data)
    return redirect('/show/recipes')

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    Recipe.delete_one({'id': id})
    return redirect('/show/recipes')

@app.route('/edit/recipe/<int:id>')
def render_edit_recipe(id):
    return render_template('edit_recipe.html', recipes = Recipe.get_one({'id': id}))

@app.route('/update/recipe', methods=['post'])
def edit_recipe():
    Recipe.update_one(request.form)
    return redirect ('/show/recipes')

