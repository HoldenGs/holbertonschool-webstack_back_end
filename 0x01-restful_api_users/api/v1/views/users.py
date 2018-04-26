
from api.v1.views import app_views
from models.user import User
from flask import jsonify, abort, request
from models import db_session

@app_views.route("/users", methods=["GET"], strict_slashes=False)
def users_list():
	return jsonify([user.to_dict() for user in User.all()])

@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def user_get(user_id):
	user = User.get(user_id)
	if user is None:
		abort(404)
	return jsonify(user.to_dict())

@app_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def user_delete(user_id):
	user = User.get(user_id)
	if user is None:
		abort(404)
	db_session.delete(user)
	db_session.commit()
	return jsonify({})

@app_views.route("/users", methods=["POST"], strict_slashes=False)
def user_create():
	# required_fields = ['email', 'password', 'first_name', 'last_name']
	data = request.get_json()
	if data is None:
		return jsonify({"error": "Wrong format"}), 400
	if data.get('email') is None:
		return jsonify({"error": "email missing"}), 400
	if data.get('password') is None:
		return jsonify({"error": "password missing"}), 400
	print(data.get('email'))
	try:
		# user = User({key: value for key, value in data.items() if key in required_fields})
		user = User()
		user.email = data.get('email')
		user.password = data.get('password')
		user.first_name = data.get('first_name')
		user.last_name = data.get('last_name')
		db_session.add(user)
		db_session.commit()
	except BaseException as e:
		return jsonify({"error": "Can't create User: {}".format(e)}), 400
	return jsonify(user.to_dict()), 201

@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def user_update(user_id):
	user = User.get(user_id)
	data = request.get_json()
	if user is None:
		abort(404)
	if data is None:
		return jsonify({"error": "Wrong format"}), 400
	user.first_name = data.get('first_name')
	user.last_name = data.get('last_name')
	return jsonify(user.to_dict())
