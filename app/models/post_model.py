from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient, ReturnDocument
from typing import Union
from os import getenv
import pymongo

from app.exceptions.post_exceptions import PostIdNotFound 

cluster = MongoClient(getenv("DATABASE_URI"))

db = cluster["kenzie"]

collection = db["posts"]

class Post:
    def __init__(self, title, author, tags, content) -> None:
        self.title = title
        self.author = author
        self.tags = tags 
        self.content = content
        self.created_at = datetime.now().strftime("%d/%m/%Y - %X")
        self.updated_at = self.created_at

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

    def create_post(self):
        db.posts.insert_one(self.__dict__)

    @staticmethod
    def delete_post(post_id: str):
        post_to_be_deleted = db.posts.find_one_and_delete({"_id": ObjectId(post_id)})
        
        return post_to_be_deleted

    @staticmethod
    def update_post(post_id: str, payload: dict):

        post_to_be_updated = db.posts.find_one_and_update(
            {"_id": ObjectId(post_id)},
            {"$set": payload},
            return_document=ReturnDocument.AFTER,
        )
        if not post_to_be_updated:
            raise PostIdNotFound 
            
        return post_to_be_updated