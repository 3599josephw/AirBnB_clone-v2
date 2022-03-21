#!/usr/bin/python3
"""Task 2 - c_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Returns on main page"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns on /hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """Returns on /c/<text>"""
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host="0.0.0.0")
