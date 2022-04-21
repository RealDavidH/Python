from flask import redirect
from flask_app import app
from flask_app.controllers import author_controller, book_controller, route_controller
if __name__ == "__main__":
    app.run(debug=True)