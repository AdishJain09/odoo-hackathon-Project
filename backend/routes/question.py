from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.stackit
questions = db.questions

question_bp = Blueprint('question', __name__)

@question_bp.route('/questions', methods=['POST'])
@jwt_required()
def ask_question():
    data = request.json
    identity = get_jwt_identity()
    question = {
        "title": data["title"],
        "description": data["description"],
        "tags": data["tags"],
        "votes": 0,
        "answers": [],
        "accepted": None,
        "author": identity["email"]
    }
    questions.insert_one(question)
    return jsonify(msg="Question posted")

@question_bp.route('/questions', methods=['GET'])
def get_questions():
    return jsonify([{
        "_id": str(q["_id"]),
        **{k: q[k] for k in q if k != "_id"}
    } for q in questions.find()])
