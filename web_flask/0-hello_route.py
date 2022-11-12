#!/usr/bin/python3
<<<<<<< HEAD
"""
0. Hello Flask!
This module uses Flask and starts 
a Flask web application
"""


from flask import Flask
=======
"""This is a simple flask application"""

from flask import Flask


>>>>>>> 79d9bb2506d5c37457eac732697cc5dc79c1c83b
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_hbnb():
    """response text"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
=======
def index():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 79d9bb2506d5c37457eac732697cc5dc79c1c83b
