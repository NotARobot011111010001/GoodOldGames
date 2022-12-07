from pymongo import MongoClient
from bson.json_util import dumps
from flask import Blueprint, request, jsonify
import os
import requests
import json
# end imports

cluster = MongoClient(
    "mongodb+srv://admin:axCyth27ZUkPrWM@advdevapp.v35rz2w.mongodb.net/?retryWrites=true&w=majority") # link to access, read and write to MongoDB

db = cluster["GameStore"] # database name

collection = db["GameInfo"] 


# Cloud function to get a forum posts from mongo
def get_mongodb_items(game_name):
    #game_name = request.form['game-name']

    # create queries
    game_query = {"game": {"$regex": game_name}}
    #title_query = {"title": {"$eq": "Man walks on the moon"}}
    #author_query = {"author": {"$eq": "Faker"}}
    #dateCreated_query = {"dateCreated": {"$eq": 2022}}

    myCursor = collection.find( game_query ) # finds the closest matching game name

    list_cur = list(myCursor)
    print(list_cur)

    json_data = dumps(list_cur)

    return json_data

def store_mongodb(game, title, author, dateCreated,thumbnail, content): # writes reviews to MongoDB
    # Write to MongoDB
    json_data = {"game": game, "title": title, "author":
    author, "dateCreated": dateCreated, "thumbnal": thumbnail, "content": content}
    collection.insert_one(json_data)



