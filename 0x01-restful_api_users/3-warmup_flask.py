#!/usr/bin/env python3

from flask import Flask, jsonify
from os import environ

app = Flask(__name__)

@app.route('/hbtn', methods=['GET'], strict_slashes=False)
def index():
	return jsonify({"C": "is fun", "Python": "is cool",
		"Sysadmin": "is hiring"})


if __name__ == "__main__":
	host = environ.get('HBNB_API_HOST')
	port = int(environ.get('HBNB_API_PORT'))
	app.run(host=host, port=port)
