from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World, Vietnam</h1>"

@app.route("/about/<username>")
def about(username):
    return f'<h1>Hello, this is page about {username}</h1>'