from app.exceptions.post_exceptions import PostIdNotFound
from app.posts_package.posts_service import validate_keys, validated_id
from app.models.post_model import Post
from flask import jsonify, request
from datetime import datetime
from http import HTTPStatus

def get_all_posts():

    posts_list = Post.get_all_posts()
    posts_list = list(posts_list)

    return jsonify(posts_list), HTTPStatus.OK

def post_by_id(post_id):

    try:

        chosen_post = Post.get_post_by_id(post_id)

        if not chosen_post:
            return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND
        
        return chosen_post, HTTPStatus.OK

    except ValueError:
        return {"error": "A ID precisa ser um número"}, HTTPStatus.BAD_REQUEST

def create_post():

    expected_keys = {"title", "author", "tags", "content"}
    data = request.get_json()

    try: 
        validate_keys(data, expected_keys)
        post = Post(**data)
    except KeyError as error:
        return error.args[0], HTTPStatus.BAD_REQUEST

    post.create_post()

    return post.__dict__, HTTPStatus.CREATED

def delete_post(post_id):

    try: 

        post_to_be_deleted = Post.delete_post(post_id)

        if not post_to_be_deleted:
            return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND

        return post_to_be_deleted, HTTPStatus.OK

    except ValueError:
        return {"error": "A ID precisa ser um número"}, HTTPStatus.BAD_REQUEST

def update_post(post_id):

    data = request.get_json()
    data["updated_at"] = datetime.now().strftime("%d/%m/%Y - %X")
    
    try: 
        post_to_be_updated = Post.update_post(post_id, data)
        return post_to_be_updated, HTTPStatus.OK
    
    except PostIdNotFound:
        return {"error": f"id {post_id} not found"}, HTTPStatus.NOT_FOUND
    
    except ValueError:
        return {"error": "A ID precisa ser um número"}, HTTPStatus.BAD_REQUEST
