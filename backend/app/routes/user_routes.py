from flask import Blueprint
from app.controllers.user_controller import get_users

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/", methods=["GET"])(get_users)
