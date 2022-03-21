#!/usr/bin/python3
"""Task 9 - states"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False

states = storage.all(State)


@app.route("/states")
@app.route("/states/<id>")
def cities_list(id=None):
    """returns html page of states or cities in a state"""
    flag = 0
    return render_template('9-states.html', states=states, id=id, flag=flag)


@app.teardown_appcontext
def teardown(appcontext):
    """shuts down database"""
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0")