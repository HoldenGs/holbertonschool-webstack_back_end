
from api.v1.views import app_views
from flask import jsonify
from models import *
from models.user import User

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
	return jsonify({"status": "OK"})

@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def stats():
	return jsonify({"users": User.count()})
