#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
