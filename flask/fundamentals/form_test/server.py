
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'Super secret key'

@app.route('/')          
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print('got post info')
    print(request.form)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show():
    print(session['username'], session['useremail'])
    return render_template('show.html')


#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 