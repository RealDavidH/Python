from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "kekekekekek"

@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['langauge'] = request.form['language']
    session['comment'] = request.form['comment']
    if 'check' in request.form:
        session['check'] = request.form['check']
    else:
        session['check'] = 'off'
    print(session)
    return redirect ('/results')

@app.route('/results')
def results():
    return render_template('results.html')
#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 