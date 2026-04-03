from flask import Blueprint, jsonify

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/', methods=['GET'])
def fetch():
    return jsonify({"message": "Hello World"})
