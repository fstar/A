from flask import Blueprint, jsonify

heart_bp = Blueprint('heart_bp', __name__, url_prefix="/heart")


@heart_bp.route("/")
def heart():
    return "ok"
