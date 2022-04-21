from flask import redirect
from flask_app import app
from flask_app.controllers import sighting_controller, user_controller, routes, skeptic_controller
if __name__ == "__main__":
    app.run(debug=True)