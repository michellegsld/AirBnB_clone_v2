#!/usr/bin/python3
"""
3-python_route.py
Task 3:
A script that starts a Flask web application
"""
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def index(strict_slashes=False):
    """
    Main route and what it displays
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb(strict_slashes=False):
    """
    Route that displays HBNB
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text, strict_slashes=False):
    """
    Route that displays C + <text>
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool', strict_slashes=False):
    """
    Route that displays Python + <text>
    """
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)