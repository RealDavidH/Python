from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')          
def hello_world():
    return redirect('/play')

@app.route('/play')
def play():
    
    return render_template('index.html',phrase="Welcome!", times=3)

@app.route('/play/<x>')
def playnums(x):
    x = int(x)
    return render_template('index.html',phrase="Welcome!", times=x)
@app.route('/play/<x>/<colors>')
def color(x,colors):
    x = int(x)
    return render_template('index.html',phrase="Welcome!", times=x, color=colors)

#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True)