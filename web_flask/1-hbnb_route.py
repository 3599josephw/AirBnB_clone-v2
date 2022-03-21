#!/usr/bin/python3
"""Task 1 - hbnb route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"

if '__name__' == '__main__':
    app.run(host="0.0.0.0")
