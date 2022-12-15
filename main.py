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


@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/games_info')
def games_mongoDB(): 
    """ USES "GET"
    - GETs game information from mongodb using Google Cloud Functions!
    """

    url = "https://europe-west2-advanceddev-011111010001.cloudfunctions.net/function-1"

    url_Response = requests.get(url)

    json_response = url_Response.text
    print(json_response)

    data = json.loads(json_response)
    print(data)

    return render_template('gamesinfo.html', data=data)

@app.route('/reviews', methods=["GET"])
def reviews():
    if request.method == "GET":
        #return get_mongodb_items()
        data = json.loads(get_mongodb_items()) # gets data from mongoDB python function
        return render_template('reviews.html', data=data)
    else:
        return render_template('reviews.html')

@app.route('/createpost', methods=['POST', 'GET'])
def createPost():
    """
    Creates a review based on user input and stores it in MongoDB
    - Uses jsonify to store it in MongoDB
    - Returns: message saying "Post Submitted"
    """
    game_name = request.form['game_name']
    title = request.form['title']
    author = request.form['author']
    dateCreated = datetime.datetime.now().year
    content = request.form['content']

    json_stuff = jsonify(game_name, title, author, dateCreated, content)
    # print(json_stuff)

    if game_name and title and author and content:
        store_post_mongodb(game_name, title, author, dateCreated, content)
    return jsonify({'message': "Post submitted!"})

@app.route('/deletereview', methods=['POST'])
def delete_reviews():
    """
    Deletes reviews from MongoDB
    """
    stuff = jsonify(store_post_mongodb())
    print(stuff)


@app.route("/mongo", methods = ["GET"])
def mesh_mongo():
    """
    Gets reviews from MongoDB using Google Cloud Functions!
    TODO: Add the reviews to an html file (reviews_mongoDB.html)
    """
    url = "https://europe-west2-advanceddev-011111010001.cloudfunctions.net/Service_Mesh_Layer_Function"
    req = requests.post(url, json = {
        "source": "mongo",
        }, headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
            })
    return req.content

@app.route("/google", methods = ["GET"])
def mesh_google():
    """
    Gets reviews from Google Storage Buckets using Google Cloud Functions!
    TODO: Add the reviews to a webpage (reviews_googlebucket.html)
    """
    url = "https://europe-west2-advanceddev-011111010001.cloudfunctions.net/Service_Mesh_Layer_Function"
    
    req = requests.post(url, json = {
        "source": "google",
        }, headers = {
            "Content-type": "application/json",
            "Accept": "text/plain"
        })
    return (req.content)

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
