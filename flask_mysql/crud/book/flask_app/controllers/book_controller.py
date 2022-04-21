from ast import Return
from flask_app import app, DATABASE, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_book import Book


@app.route('/books')
def book():
    return render_template('books.html', books = Book.get_all())

@app.route('/book/create', methods=['post'])
def create_book():
    id = Book.create(request.form)
    return redirect(f'/book/{id}')

