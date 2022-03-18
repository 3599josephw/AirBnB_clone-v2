"""Task 2 - c_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))

app.run(host="0.0.0.0")
