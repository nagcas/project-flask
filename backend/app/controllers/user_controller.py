from flask import jsonify
from app.services.user_service import fetch_all_users

def get_users():
    users = fetch_all_users()
    return jsonify(users), 200