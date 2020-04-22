#!/usr/bin/python3
"""
7-states_list.py
Task 7:
A script that starts a Flask web application
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlalchemy(self):
    storage.close()


@app.route('/states_list')
def list_states(strict_slashes=False):
    """
    Route that displays a list of:
    All State objects present in DBStorage, sorted by name
    """
    states_dict = storage.all(State)
    return render_template("7-states_list.html", list=states_dict.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
