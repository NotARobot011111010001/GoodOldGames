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

mongoDB_collection = db["GameReviews"] 


# Cloud function to get a forum posts from mongoDB
def get_mongodb_items():
    """
    Gets reviews from MongoDB
    """
    #game_name = request.form['game-name']
    # create queries
    
    title_query = {"game": {"$in": ["Cyberpunk 2077", "The Witcher 3: Wild Hunt", "Battlefield 4", "Battlefield 2042", "Assasin's Creed Origins", "Assasin's Creed Black Flag" ]}}
    dateCreated_query = {"dateCreated": {"$gt": 2010}}
    myCursor = mongoDB_collection.find({"$and": [title_query, dateCreated_query]})

    list_cur = list(myCursor)
    #print(list_cur)
    
    json_data = dumps(list_cur)
    return json_data

def store_post_mongodb(game_name, title, author, dateCreated, content):
    """
    Stores the post into Mongo collection
    - writes reviews to MongoDB
    """
    # Write to MongoDB
    json_data_to_mongoDB = {"game": game_name, "title": title, "author": author, "dateCreated": dateCreated, "content": content}

    print(json_data_to_mongoDB)
    mongoDB_collection.insert_one(json_data_to_mongoDB)



