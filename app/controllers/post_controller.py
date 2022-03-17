from http import client
from flask import request, jsonify
import pymongo 

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]

collection = db["posts"]

def post():
    data = request.get_json()
    db.crud.insert_one(data)
    del data["_id"]
    return jsonify(data), 201