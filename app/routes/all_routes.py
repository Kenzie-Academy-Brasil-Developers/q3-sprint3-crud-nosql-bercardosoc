from flask import Flask

def all_routes(app: Flask):
    
    @app.get("/posts")
    def read_all_posts():
        return ""

    @app.get("/posts/<post_id>")
    def read_a_post(post_id):
        return ""

    @app.post("/posts")
    def post_a_post():
        return ""

    @app.patch("/posts/<post_id")
    def update_a_post():
        return ""

    @app.delete("/posts/<post_id")
    def delete_a_post():
        return ""