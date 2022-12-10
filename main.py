from flask import Flask, render_template, jsonify, request, make_response
import sys, json, datetime
from sql_db import get, create
import logging
from pymongo import MongoClient
from mongodb import *
from bson.json_util import dumps
#from google.cloud import datastore


#firebase_request_adapter = requests.Request()
# [END gae_python3_auth_verify_token]
# [END gae_python38_auth_verify_token]
#datastore_client = datastore.Client()

app = Flask(__name__)
"""
Loading HTML pages.
"""


@app.route('/')
def index():  # put application's code here
    """
    Loads the home page for the game store
    """
    return render_template("home.html")


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
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

    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def form():
    return render_template('register.html')


@app.route('/reviews', methods=["GET"])
def reviews():
    if request.method == "GET":
        #return get_mongodb_items()
        data = json.loads(get_mongodb_items()) # gets data from mongoDB python function
        return render_template('reviews.html', data=data)

    return render_template('reviews.html')#, jsonify(game_name)    

@app.route('/createpost', methods=['POST', 'GET'])
def createPost():
    #game_name = request.form['game']
    game_name = "Cyberpunk 2077" """ Need to fix this later, for now it works and saves to MongoDB!!! """
    title = request.form['title']
    author = request.form['author']
    dateCreated = datetime.datetime.now().year
    content = request.form['content']
    
    print(title, author, content, dateCreated, game_name)

    json_stuff = jsonify(game_name, title, author, dateCreated, content)
    print(json_stuff)

    if game_name and title and author and content:
        store_post_mongodb(game_name, title, author, dateCreated, content)
    return jsonify({'message': "Post submitted!"})

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
    app.run(host="localhost", port=8080, debug=True)
