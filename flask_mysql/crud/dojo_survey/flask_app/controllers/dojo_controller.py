from flask_app import app, DATABASE
from flask import render_template, request, redirect, session, flash
from flask_app.models.model_dojo import Dojo


@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    if not Dojo.validate(request.form):
        return redirect('/form')
    id = Dojo.create(request.form)
    return redirect(f'/results/{id}')

@app.route('/results/<int:id>')
def show_results(id):
    
    return render_template('results.html', info=Dojo.getinfo({'id': id}))