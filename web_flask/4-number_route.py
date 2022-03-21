#!/usr/bin/python3
"""Task 4 - number_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """Returns text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """Returns given text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """returns number if its an integer"""
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
