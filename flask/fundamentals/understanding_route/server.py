import string
from flask import Flask
from flask import request
app = Flask(__name__)


route_list=["/dojo",
            "/say/'word'(word can be any word you want)", 
            "/repeat/'num'/'word' (enter a number in place of num, and a word in place of word)"]



@app.route('/')
def hello_world():
    return f'The routes you may enter are {route_list}'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<word>')
def say(word):
    str(word)
    if word == "flask":
        return "Hi Flask"
    if word == "michael":
        return "Hi Michael"
    if word == "john":
        return "Hi John"

@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    tempstr = ''
    number = int(number)
    if isinstance(number, int) and isinstance(word, str):
        for i in range(0,number):
            tempstr += word
        return tempstr
    else:
        return "error"


#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 