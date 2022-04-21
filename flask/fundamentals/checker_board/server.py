from tokenize import Number
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<number1>')
@app.route('/<number1>/<number2>')
@app.route('/<number1>/<number2>/<color1>')
@app.route('/<number1>/<number2>/<color1>/<color2>')
def hello_world(number1=8, number2=8, color1="red", color2="black"):
    num1 = int(number1)
    num2 = int(number2)
    clr1 = color1
    clr2= color2
    return render_template('index.html', color=clr1, color2=clr2, number1=num1, number2=num2)
    
#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 