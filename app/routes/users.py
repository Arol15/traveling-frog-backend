from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from ..models import db, User
from ..auth import require_auth

bp = Blueprint("users", __name__, url_prefix='/api/users')

@bp.route('') #fetch all users
# @require_auth
def users(): 
    users = User.query.all()
    users = [user.to_dict() for user in users]
    return {"data": {'users': users}, "error": None}
    # return jsonify(users)

@bp.route('/<int:userId>') # fetch a single user
def user(userId):
    user = User.query.filter(User.id == userId).one()
    return {'user': user.as_dict()}

@bp.route('/<string:email>') # fetch a single user
def email(email):
    user = User.query.filter(User.email == email).one()
    return {"data": {'user': user.as_dict()}}

@bp.route('/<int:userId>', methods=['PUT'])  # make changes to an existing user
def edit_user(userId):
    users = request.json
    print(users)
    user = User.query.filter(User.id == userId).one()
    print(user)
    if user:
        user.first_name = users['first_name']
        user.last_name = users['last_name']
        user.image = users['image']
        user.email = users['email']
        # user.password = data['password']
        db.session.commit()
        return {'user': user.as_dict()}
    # except AssertionError as message:
    #     print(str(message))
    else: 
        return jsonify(message="check your entries"), 400