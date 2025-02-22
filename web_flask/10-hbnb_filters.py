#!/usr/bin/python3
"""Task 10 - hbnb_filters"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False

states = storage.all(State)
amenities = storage.all(Amenity)


@app.route("/hbnb_filters")
def filters():
    """Returns html page with dropdown of states and cities"""
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(appcontext):
    """shuts down database"""
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
