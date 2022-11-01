from flask import Flask, render_template, jsonify, request, make_response
import sys, json
from db import get, create
import logging
# from werkzeug.wrappers import response

app = Flask(__name__)
"""
Loading HTML pages.
"""


@app.route('/')
def index():  # put application's code here
    return render_template("home.html")


@app.route('/home')
@app.route('/')
def home():
    """
    loads the main page of the website
    :return: main page of website
    """
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    login method for login page - loads login page and input from login form
    :return: login page
    """
    if_error = render_template('404.html')  # if something goes wrong,this will show

    #if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
    #    username = request.form['username']  # requesting username & password using the .form from <form> in HTML
    #    password = request.form['password']

    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def form():
    return render_template('register.html')


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email
    )
    # [END render_template]


app.route('/store', methods=['GET'])
def get_games():
    """
    Gets all the games list from the database
    :return: games from database
    """
    return get()


@app.route('/add', methods=['POST'])
def add_game():
    """
    adds the game information to the table
    :return: Game added message
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    create(request.get_json())
    return 'Game Added'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=5000, debug=True)
