from flask_app import app, DATABASE, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_author import Author
from flask_app.models.model_book import Book
from flask_app.models.model_favorite import Favorite

@app.route('/')
def redirect_authors():
    return redirect ('/authors')

@app.route('/author/<int:id>/favorite')
def show_author(id):
    return render_template('show_authors.html', authors = Author.get_one({"id": id}), books = Book.get_all(), favorites = Favorite.get_one_author_id({'id':id}))

@app.route('/author/add/favorite', methods = ['post'])
def add_favorite():
    id = request.form['author_id']
    if not Favorite.validate(request.form):
        return redirect(f'/author/{id}/favorite')
    Favorite.create(request.form)
    return redirect(f'/author/{id}/favorite')


@app.route('/author/add/book/favorite', methods = ['post'])
def add_favorite_book():
    id = request.form['book_id']
    if not Favorite.validate(request.form):
        return redirect(f'/book/{id}')
    Favorite.create(request.form)
    return redirect(f'/book/{id}')

@app.route('/book/<int:id>')
def show_books(id):
    print(Favorite.get_one_author_id({'id':id}))
    return render_template("show_books.html", books = Book.get_one({"id": id}), authors = Author.get_all(), favorites = Favorite.get_one_book_id({'id':id}))