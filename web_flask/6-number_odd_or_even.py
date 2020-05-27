#!/usr/bin/python3
"""
6-number_odd_or_even.py
Task 6:
A script that starts a Flask web application
"""
from flask import Flask, render_template, abort

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


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_n(n):
    """
    Route that displays an HTML page
    But only if <n> is an integer
    """
    if n.isdigit():
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route that displays an HTML page if <n> is an integer
    What is printed depends on if <n> is even or odd
    """
    if n.isdigit():
        file = '6-number_odd_or_even.html'
        if int(n) % 2 == 0:
            string = "{} is even".format(n)
        else:
            string = "{} is odd".format(n)
        return render_template(file, string=string)
    abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
