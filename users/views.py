from flask import Blueprint, jsonify

mod = Blueprint('users', __name__, url_prefix='/users')

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@mod.route('/', methods=['GET'])
def fetch():
    return jsonify(users)
