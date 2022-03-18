from datetime import datetime
from http import HTTPStatus
from flask import jsonify, request
from app.exceptions.post_exceptions import PostIdNotFound
from app.models.post_model import Post
from app.posts_package.posts_service import validate_keys

def get_all_posts():

    posts_list = Post.get_all_posts()
    posts_list = list(posts_list)

    for post in posts_list:
        Post.serialize_post(post)

    return jsonify(posts_list), HTTPStatus.OK

def post_by_id(post_id: str):

    if len(post_id) != 24:
        return {"error": "ID inválido. Por favor insira 24 caracteres"}
    
    chosen_post = Post.get_post_by_id(post_id)

    if not chosen_post:
        return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND
    
    Post.serialize_post(chosen_post)
    
    return chosen_post, HTTPStatus.OK

def create_post():

    expected_keys = {"title", "author", "tags", "content"}
    data = request.get_json()

    try: 
        validate_keys(data, expected_keys)
        post = Post(**data)
    except KeyError as error:
        return error.args[0], HTTPStatus.BAD_REQUEST
        #return {"error": "Erro de chave"}, HTTPStatus.BAD_REQUEST

    post.create_post()

    serialized_post = Post.serialize_post(post)

    return serialized_post.__dict__, HTTPStatus.CREATED

def delete_post(post_id: str):

    if len(post_id) != 24:
        return {"error": "ID inválido. Por favor insira 24 caracteres"}
    
    post_to_be_deleted = Post.delete_post(post_id)

    if not post_to_be_deleted:
        return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND


    Post.serialize_post(post_to_be_deleted)

    return post_to_be_deleted, HTTPStatus.OK

def update_post(post_id: str):

    if len(post_id) != 24:
        return {"error": "ID inválido. Por favor insira 24 caracteres"}

    data = request.get_json()
    data["updated_at"] = datetime.now().strftime("%d/%m/%Y - %X")
    
    try: 
        post_to_be_updated = Post.update_post(post_id, data)
    except PostIdNotFound:
        return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND

    serialized_post = Post.serialize_post(post_to_be_updated)

    return serialized_post, HTTPStatus.OK