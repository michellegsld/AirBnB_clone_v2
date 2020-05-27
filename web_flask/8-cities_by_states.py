#!/usr/bin/python3
"""
8-cities_by_states.py
Task 8:
A script that starts a Flask web application
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlalchemy(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities():
    """
    Route that displays all City objects linked to a State
    """
    states_dict = storage.all(State)
    list_sorted = sorted(states_dict.values(), key=lambda obj: (obj.name))
    return render_template("8-cities_by_states.html", state_list=list_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
