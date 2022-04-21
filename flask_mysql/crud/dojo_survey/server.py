from flask import redirect
from flask_app.controllers import dojo_controller
from flask_app import app


@app.route('/')
def re_redirect():
    return redirect('/form')


if __name__ == "__main__":
    app.run(debug=True)