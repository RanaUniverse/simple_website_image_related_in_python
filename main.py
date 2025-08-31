from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask (By Default)")
    age = request.args.get("age", 00)
    return f"Hello, {escape(name)}, Your Age is: {age}"


@app.route("/user/<username>")
def show_user_profile(username: str | int | None):
    # show the user profile for that user
    return f"User is this whose username is: {escape(username)}"


# @app.route("/post/<int:post_id>")
# def show_post(post_id:int):
#     # show the post with the given id, the id is an integer
#     return f"Post with integer value: {post_id}"


@app.route("/post/<int:post_id>")
def show_post_int(post_id: int):
    return f"🔢 Post with integer value: {post_id}"


@app.route("/post/<string:post_id>")
def show_post_str(post_id: str):
    return f"🔤 Post with string value: {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath: str):
    # show the subpath after /path/
    return f"Subpath is like the file path: {escape(subpath)}"
