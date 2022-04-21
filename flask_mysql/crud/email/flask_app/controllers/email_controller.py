from types import NoneType
from flask_app import app, DATABASE
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_email import Email
import re

@app.route('/')
def create_email():
    return render_template('index.html')

@app.route('/email/process', methods=['post'])
def process_email():
    if not Email.validate(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect ('/email/show')

@app.route('/email/show')
def show_emails():
    emails = Email.get_all()
    if isinstance(emails, NoneType):
        return render_template('show.html')
    return render_template('show.html', emails = emails)

@app.route('/delete/email/<int:id>')
def delete_email(id):
    Email.delete_one({"id":id})
    return redirect('/email/show')

