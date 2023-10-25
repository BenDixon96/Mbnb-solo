import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def submit_login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    
    email = request.form['email']
    password = request.form['password']
    user = repo.get_by_email(email)
    if repo.validate_credentials(email, password) == True:
        return redirect("/spaces")


@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
