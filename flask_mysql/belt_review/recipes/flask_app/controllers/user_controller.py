from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_user import User

@app.route('/')
def login_page():
    return render_template('frontpage.html')

@app.route('/create/user', methods=['post'])
def create_user():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': pw_hash
    }
    id = User.create(data)
    session['uuid'] = id
    return redirect('/show/recipes')

@app.route('/user/login', methods=['post'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    id = session['uuid']
    return redirect('/show/recipes')


@app.route('/logout')
def logout():
    if 'id' in session:
        session.clear()
        return redirect('/')
    return redirect('/')