from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Union
from os import getenv
import pymongo 

cluster = MongoClient(getenv("DATABASE_URI"))

db = cluster["kenzie"]

collection = db["posts"]

class Post:
    def __init__(self, title, author, tags, content) -> None:
        self.title = title
        self.author = author
        self.tags = tags 
        self.content = content

        # Serão preenchidas automaticamente:
        # id, created_at, updated_at
        
    @staticmethod
    def serialize_post(post: Union["Post", dict]):
        if type(post) is dict:
            post.update({"_id": str(post["_id"])})
        elif type(post) is Post:
            post._id = str(post._id)

        return post 

    @staticmethod
    def get_all_posts():
        
        posts_list = db.posts.find()
        return posts_list

    @staticmethod
    def get_post_by_id(post_id: str):
        chosen_post = db.posts.find_one({"_id": ObjectId(post_id)})
        return chosen_post