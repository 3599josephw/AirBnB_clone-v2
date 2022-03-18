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
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown():
    storage.close()

app.run(host="0.0.0.0")
