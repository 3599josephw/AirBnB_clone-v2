#!/usr/bin/python3
"""Task 3 - python_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Returns Hello HBNB on main page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns HBNB on /hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """Returns given text on /c/<text>"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """Returns given text on /python/"""
    return "Python {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
