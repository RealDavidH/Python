
from flask import Flask, render_template, session, request, redirect 
app = Flask(__name__) 
app.secret_key = 'kekekekeke'


@app.route('/')
def hello_world():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html', counter=session['count']) 



@app.route('/add_2')
def add_2():
    session['count'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    session['count'] = 0
    return redirect('/')

@app.route('/addnum', methods=['POST'])
def addnum():
    print(request.form)
    data = int(request.form['number'])
    session['count'] += data -1
    return redirect('/')


# def hello_world():
    # number = 0
    # number += 1
    # session['count'] += number
    # return render_template('index.html', count=session['count'])  
#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 
    
    