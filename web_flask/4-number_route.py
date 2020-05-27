#!/usr/bin/python3
"""
4-number_route.py
Task 4:
A script that starts a Flask web application
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route('/',strict_slashes=False)
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Route that displays Python + <text>
    """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """
    Route that displays <n> + is a number
    But only if <n> is an integer
    """
    if n.isdigit():
        return '{} is a number'.format(n)
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
