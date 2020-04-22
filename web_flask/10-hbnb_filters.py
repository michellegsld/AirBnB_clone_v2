#!/usr/bin/python3
"""
10-hbnb_filters.py
Task 10:
A script that starts a Flask web application
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlalchemy(self):
    storage.close()


@app.route('/hbnb_filters')
def filters(strict_slashes=False):
    """
    Route that displays info in the filters
    """
    file = "10-hbnb_filters.html"
    states_dict = storage.all(State)
    amenity_dict = storage.all(Amenity)
    s_list = sorted(states_dict.values(), key=lambda obj: (obj.name))
    a_list = sorted(amenity_dict.values(), key=lambda obj: (obj.name))
    return render_template(file, amenity_list=a_list, state_list=s_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
