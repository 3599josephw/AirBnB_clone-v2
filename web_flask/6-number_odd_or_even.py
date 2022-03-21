#!/usr/bin/python3
"""Task 6 - number_odd_or_even"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """returns hbnb"""
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
    """returns number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """returns html page with number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def even_odd(n):
    """returns html page with number odd or even"""
    if n % 2 == 0:
        status = "is even"
    else:
        status = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, status=status)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
