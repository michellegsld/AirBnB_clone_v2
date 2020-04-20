#!/usr/bin/python3
"""
0-hello_route.py
Task 0:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
