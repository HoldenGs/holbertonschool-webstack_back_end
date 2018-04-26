
from api.v1.views import app_views
from flask import Flask, jsonify
from os import environ
from models import db_session

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify({ "error": "Not found" }), 404

@app.teardown_appcontext
def close_db(e):
	db_session.remove()

if __name__ == "__main__":
	port = int(environ.get("HBNB_API_PORT"))
	host = environ.get("HBNB_API_HOST")
	app.run(port=port, host=host)
