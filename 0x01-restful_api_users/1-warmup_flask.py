#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/c', methods=['GET'], strict_slashes=False)
def index():
	return "C is fun!"

if __name__ == "__main__":
	app.run()
