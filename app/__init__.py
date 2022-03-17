from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False

    routes.init_app(app)

    """ @app.get("/posts")
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
        return "" """

    return app 