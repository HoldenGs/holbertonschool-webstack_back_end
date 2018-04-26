#!/usr/bin/env python3

from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def index():
	return "Holberton School"

@app.route('/c', methods=['GET'], strict_slashes=False)
def c():
	return "C is fun!"

if __name__ == "__main__":
	host = environ.get('HBNB_API_HOST')
	port = int(environ.get('HBNB_API_PORT'))
	app.run(host=host, port=port)
