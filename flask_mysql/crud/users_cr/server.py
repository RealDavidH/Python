from flask import redirect
from __int__ import app
from controllers import user_controller

@app.route('/')
def createpage():
    return redirect('/create_user')

if __name__ == "__main__":
    app.run(debug=True)

