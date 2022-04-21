from flask_app import app, DATABASE, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_author import Author


@app.route('/authors')
def render_authors():
    return render_template('authors.html', authors = Author.get_all())

@app.route('/create/author', methods=['post'])
def create_author():
    id = Author.create(request.form)
    return redirect ('/authors')