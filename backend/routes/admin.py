from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.stackit
questions = db.questions

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/delete-question/<id>', methods=['DELETE'])
@jwt_required()
def delete_question(id):
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify(error="Unauthorized"), 403
    questions.delete_one({"_id": ObjectId(id)})
    return jsonify(msg="Deleted successfully")
