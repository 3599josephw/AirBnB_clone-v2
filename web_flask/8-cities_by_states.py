#!/usr/bin/python3
"""Task 8 - cities_by_states"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

states = storage.all(State)


@app.route("/cities_by_states")
def cities_list():
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown():
    storage.close()

if '__name__' == '__main__':
    app.run(host="0.0.0.0")
