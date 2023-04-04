from pymongo import MongoClient
from bson.json_util import dumps
from flask import Blueprint, request, jsonify
import os
import requests
import json
# end imports

cluster = MongoClient(
    "mongodb+srv://admin:###########@advdevapp.v35rz2w.mongodb.net/?retryWrites=true&w=majority") # link to access, read and write to MongoDB

db = cluster["GameStore"] # database name

mongoDB_collection = db["GameReviews"] 


# Cloud function to get a forum posts from mongoDB
def get_mongodb_items():
    """
    Gets reviews from MongoDB
    """
    myCursor2 = mongoDB_collection.find()

    list_cur2 = list(myCursor2)
    
    json_data = dumps(list_cur2)
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

def delete_review_mongodb(game_name, title, author, dateCreated, content):
    """
    Deletes the post from Mongo collection
    - deletes reviews from MongoDB
    """
    # Write to MongoDB
    json_data_to_delete = {"game": game_name, "title": title, "author": author, "dateCreated": dateCreated, "content": content}

    print(json_data_to_delete)
    mongoDB_collection.delete_one(json_data_to_delete)