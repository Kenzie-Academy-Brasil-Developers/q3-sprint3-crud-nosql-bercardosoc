from http import HTTPStatus
from flask import jsonify, request
from app.models.post_model import Post

def get_all_posts():

    posts_list = Post.get_all_posts()
    posts_list = list(posts_list)

    for post in posts_list:
        Post.serialize_post(post)

    return jsonify(posts_list), HTTPStatus.OK

def post_by_id(post_id: str):

    chosen_post = Post.get_post_by_id(post_id)
    
    Post.serialize_post(chosen_post)
    
    return chosen_post, HTTPStatus.OK

def create_post():

    data = request.get_json()

    try: 
        post = Post(**data)
    except KeyError:
        return {"error": "Erro de chave"}, HTTPStatus.BAD_REQUEST

    post.create_post()

    serialized_post = Post.serialize_post(post)

    return serialized_post.__dict__, HTTPStatus.CREATED