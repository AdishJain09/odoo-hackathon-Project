from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.stackit
users = db.users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    users.insert_one({**data, "role": "user"})
    return jsonify(msg="User registered")

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = users.find_one({"email": data["email"], "password": data["password"]})
    if not user:
        return jsonify(error="Invalid credentials"), 401
    token = create_access_token(identity={"email": user["email"], "role": user["role"]})
    return jsonify(access_token=token)
