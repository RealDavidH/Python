from flask_app import app, DATABASE , bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_user import User

@app.route('/')
def login_page():
    return render_template('create.html')

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
    return redirect('/show/user/wall')

@app.route('/user/login', methods=['post'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    id = session['uuid']
    return redirect(f'/show/user/wall')

@app.route('/show/user/wall')
def show_user():
    return render_template('wall.html',  user = User.get_one({'id': session['uuid']}), friends = User.get_one_friend({'id': session['uuid']}), users = User.get_all(), messages = User.get_message({'id': session['uuid']}))


@app.route('/add/friend', methods=['post'])
def add_friend():
    print(request.form)
    if not User.check_friends(request.form):
        return redirect('/show/user/wall')
    User.add_friend(request.form)
    flash('Friend added!', 'add_friend')
    return redirect('/show/user/wall')

@app.route('/send/message', methods=['post'])
def send_message():
    if len(request.form['message']) <= 0:
        flash('Please enter a message', 'err_message_len')
        return redirect('/show/user/wall')
    User.send_message(request.form)
    flash('Message sent!', 'message_sent')
    return redirect('/show/user/wall')

@app.route('/delete/message/<int:id>')
def delete_message(id):
    User.delete_message({'id': id})
    flash('Message Deleted!', 'message_deleted')
    return redirect('/show/user/wall')

@app.route('/logout')
def logout():
    if 'id' in session:
        session.clear()
        return redirect('/')
    return redirect('/')