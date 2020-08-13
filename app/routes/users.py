from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from ..models import db, User
from ..auth import require_auth

bp = Blueprint("users", __name__, url_prefix='/api/users')

@bp.route('') #fetch all users
# @require_auth
def index(): 
    users = User.query.all()
    users = [user.to_dict() for user in users]
    return {'users': users}
    # return jsonify(users)

@bp.route('/<int:userId>') # fetch a single user
def get_user(userId):
    user = User.query.filter(User.id == userId).one()
    return {'user': user.as_dict()}
