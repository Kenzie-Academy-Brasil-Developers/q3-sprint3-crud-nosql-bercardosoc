from flask import request, jsonify
import pymongo 
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://ninth_avaliation:XQ4hi36Wi5mgxGk1@cluster0.nmb8m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
)

db = cluster["kenzie"]

collection = db["posts"]

def post():
    data = request.get_json()
    db.posts.insert_one(data)
    del data["_id"]
    return jsonify(data), 201