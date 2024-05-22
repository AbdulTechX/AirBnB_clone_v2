#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display 'Hello HBNB!' on the root URL.
    """
    return "hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to display 'HBNB' on the /hbnb URL.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route to display 'C ' followed by the value of the text variable,
    with underscores replaced by spaces.

    Args:
        text (str): The text to be displayed after 'C '.
    """
    return f"C{text.replace('_',' ')}"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route to display 'python' followed by the value of the text variable,
    with underscores replaced by spaces.

    Args:
        text (str): The text to be displayed after 'C '.
    """
    return f"python{text.replace('_',' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route to display 'number' followed by the value of the text variable,
    with underscores replaced by spaces.

    Args:
        number (int): The text to be displayed after 'C '.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route to display 'n is a number' using a template only if n is an integer.

    Args:
        n (int): The integer to be displayed in the message.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
