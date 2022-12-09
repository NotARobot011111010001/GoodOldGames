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
    game_query = {"content": {"$text": "/C/"}}
    #print(game_query)
      # create queries
    """title_query = {"title": {"$eq": "Best game I have ever played"}}
    author_query = {"author": {"$eq": "Powdered_Toast_Man"}}
    dateCreated_query = {"dateCreated": {"$eq": 2018}}
    myCursor = mongoDB_collection.find({"$and": [title_query, author_query, dateCreated_query]})"""
    
    title_query = {"game": {"$in": ["Cyberpunk 2077", "The Witcher 3: Wild Hunt"]}}
    dateCreated_query = {"dateCreated": {"$gt": 2017}}
    myCursor = mongoDB_collection.find({"$and": [title_query, dateCreated_query]})

    list_cur = list(myCursor)
    print(list_cur)
    
    json_data = dumps(list_cur)
    return json_data

def store_post_mongodb(game, title, author, dateCreated,thumbnail, content):
    """
    Stores the post into Mongo collection
    - writes reviews to MongoDB
    """
    # Write to MongoDB
    json_data = {"game": game, "title": title, "author": author, "dateCreated": dateCreated, "thumbnal": thumbnail, "content": content}
    mongoDB_collection.insert_one(json_data)



