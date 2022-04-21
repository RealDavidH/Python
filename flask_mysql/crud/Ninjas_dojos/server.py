from flask import redirect
from __init__ import app
from controllers import ninja_controller, dojo_controller

@app.route('/')
def re_redirect():
    return redirect('/dojos')

if __name__ == "__main__":
    app.run(debug=True)

