#!/usr/bin/python3
"""
5-number_route.py
Task 5:
A script that starts a Flask web application
"""
from flask import Flask, Markup

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


@app.route('/number/<n>')
def number_n(n, strict_slashes=False):
    """
    Route that displays <n> + is a number
    But only if <n> is an integer
    """
    if n.isdigit():
        return '{} is a number'.format(n)


@app.route('/number_template/<n>')
def number_template_n(n, strict_slashes=False):
    """
    Route that displays an HTML page
    But only if <n> is an integer
    """
    if n.isdigit():
        return Markup('<!DOCTYPE html>\n<HTML lang="en">\n    <HEAD>\n \
        <TITLE>HBNB</TITLE>\n    </HEAD>\n    <BODY> \n \
        <H1>Number: %s</H1>\n    </BODY>\n</HTML>') % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
