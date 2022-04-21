from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
DATABASE = "friendshipsdb"
app.secret_key = 'kekekekeke'
