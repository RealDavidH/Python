from flask import Flask #render_template, #request, #redirect, #session
app = Flask(**name**)

@app.route('/')
def hello_world(): return 'Hello World!'

#this needs to stay at the bottom if name=="main": app.run(debug=True)