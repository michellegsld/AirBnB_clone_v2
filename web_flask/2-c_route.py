#!/usr/bin/python3
"""
2-c_route.py
Task 2:
A script that starts a Flask web application
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Main route and what it displays
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route that displays HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route that displays C + <text>
    """
    return 'C {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
