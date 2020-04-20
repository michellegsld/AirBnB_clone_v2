#!/usr/bin/python3
"""
1-hbnb_route.py
Task 1:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
