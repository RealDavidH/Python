from urllib import request
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__) 
app.secret_key = 'kkekeke'

def makeRandNum():
    return random.randint(0, 100)

firstload = True

@app.route('/')          
def hello_world(firstload = firstload):
    if firstload:
        firstload = False
        reset()
    if session['randnum'] == 0:
        session['randnum'] = makeRandNum()
    
    num = session['randnum']
    print(num)
    return render_template('index.html', hidden1='hidden', hidden2='hidden', hidden3='hidden', hidden4='hidden', num=num)

@app.route('/test', methods=['POST'])
def check():
    
    num = int(request.form['text'])
    if session['tries'] >= 5:
        return render_template('index.html', hidden1='hidden', hidden2='hidden', hidden3='hidden', hide='hidden', num=session['randnum'])
    if session['randnum'] > num:
        session['tries'] += 1
        return render_template('index.html', hidden2='hidden', hidden3='hidden', hidden4='hidden', num=session['randnum'])
    elif session['randnum'] < num: 
        session['tries'] += 1
        return render_template('index.html', hidden1='hidden', hidden3='hidden', hidden4='hidden', num=session['randnum'])
    elif session['randnum'] == num:
        session['tries'] += 1
        return render_template('index.html', hidden1='hidden', hidden2='hidden',hide='hidden', hidden4='hidden', num=session['randnum'])
    else:
        session['tries'] += 1
        return redirect('/')

@app.route('/reset')

def reset():
    print('inside reset')
    session['tries'] = 0
    session['randnum'] = 0
    return redirect('/')

#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True)