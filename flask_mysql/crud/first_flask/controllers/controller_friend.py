from __int__ import app
from flask import render_template, request, redirect, session
from models.friend import Friend

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", allfriends=friends)

@app.route('/create_friend', methods=['post'])
def create_friend():
    Friend.create(request.form)
    return redirect('/')