#!/usr/bin/python3
"""Task 0 - Hello Route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Returns Hello HBNB!"""
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
