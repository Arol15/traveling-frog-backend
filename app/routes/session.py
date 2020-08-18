from flask import Blueprint, Response, request, jsonify
import jwt
import json
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash
from ..models import db, User
from ..config import Configuration


bp = Blueprint("session", __name__, url_prefix='/api/session')

@bp.route('/login', methods=["POST"], strict_slashes=False)  # signin/start new session 
# @cross_origin()
def login():
    data = request.json
    print(data)
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"error": "Email not found"}, 422
    print(data['password'], user.password, generate_password_hash(data['password']))
    if user.check_password(data['password']):
        access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
        return  {"data":{'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}, 'error': None}
    else:
        return {"error": "Incorrect password"}, 401

@bp.route('/signup', methods=["POST"]) # create new account
# @cross_origin()
def signup():
    data = json.loads(request.get_data().decode('UTF-8'))
    # print(json.dumps(data, indent=4, sort_keys=True)['email'])
    # data = jsonify(data)
    # email = data.get("email")
    email = data['email']
    test = User.query.filter_by(email=email).first()
    # data = request.json
    # print(f"\n\n\nDATA\n{data}\n\n\n")
    if test: 
        return jsonify(message="The user is already exist"), 409
    else:
        # print(request.form) 
        last_name = data['last_name']
        first_name = data['first_name']
        # image = data['image']
        # if image == "":
        # image = None
        hashed_password = data['password']
        user = User(password=hashed_password, email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
        # return jsonify(message="User created successfully"), 201

        access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
        return {"data": {'access_token': access_token.decode('UTF-8'), 'user': user.as_dict()}, 'error': None}

@bp.route('', methods=["DELETE"])
def logout():
    access_token = jwt.encode({'email': ''}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': ''}
    