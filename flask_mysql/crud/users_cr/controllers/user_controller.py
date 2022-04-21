from __int__ import app
from flask import render_template, request, redirect, session
from models.user import User

#Display Route
@app.route('/create_user')
def create_user():
    user = User.get_all()
    return render_template('create.html', users=user)

#Action
@app.route('/process',  methods=['post'])
def process_user():
    id = User.create(request.form)
    return redirect(f'/show_user/{id}')

#Display Route
@app.route('/show_user/<int:id>')
def show_user(id):
    user = User.getinfo({'id': id})
    return render_template('user_card.html', users=user)

#Display Route
@app.route('/account/<int:id>/edit')
def edit(id):
    user = User.getinfo({'id': id})
    print(user)
    return render_template('edit.html', users=user)

#Action Route
@app.route('/update/<int:id>', methods=['post'])
def update_user(id):
    print(request.form)
    User.update_one(request.form)
    return redirect (f'/show_user/{id}')


#Display Route
@app.route('/users')
def show_users():
    alluser = User.get_all()
    return render_template('read.html', users=alluser)

#Action Route
@app.route('/user/<int:id>/delete')
def delete_user(id):
    User.delete_one({'id': id})
    return redirect('/users')