#!/usr/bin/python3
"""Task 5 - number_template"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Returns hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """returns hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """returns given text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """returns given text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """returns given number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """returns html page with given number"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
