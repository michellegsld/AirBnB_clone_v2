#!/usr/bin/python3
"""
9-states.py
Task 9:
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


@app.route('/states')
def list_all(strict_slashes=False):
    """
    Route that displays all States
    """
    states_dict = storage.all(State)
    list_sorted = sorted(states_dict.values(), key=lambda obj: (obj.name))
    return render_template("9-states.html", state_list=list_sorted)


@app.route('/states/<id>')
def list_specific(id, strict_slashes=False):
    """
    Route that displays a State based off <id>
    """
    states_dict = storage.all(State)
    key = "State." + id
    if key not in states_dict.keys():
        return render_template("9-states.html", state_obj='None')
    else:
        s = states_dict[key]
        return render_template("9-states.html", state_list='None', state_obj=s)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
