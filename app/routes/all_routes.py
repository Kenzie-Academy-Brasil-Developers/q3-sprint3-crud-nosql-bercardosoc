from flask import Flask

from app.controllers import post_controller

def all_routes(app: Flask):
    
    @app.get("/posts")
    def read_all_posts():
        return post_controller.get_all_posts()

    @app.get("/posts/<post_id>")
    def read_a_post(post_id):
        return post_controller.post_by_id(post_id)

    @app.post("/posts")
    def post_a_post():
        return post_controller.create_post()

    @app.delete("/posts/<post_id>")
    def delete_a_post(post_id):
        return post_controller.delete_post(post_id)

    @app.patch("/posts/<post_id>")
    def update_a_post(post_id):
        return post_controller.update_post(post_id)
