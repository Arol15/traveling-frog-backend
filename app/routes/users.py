from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from ..models import db, User
from ..auth import require_auth
from ..config import Configuration
import boto3
# from s3 import upload_file

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

@bp.route('/<string:email>', methods=['POST'])  # make changes to an existing user
def edit_user(email):
    users = request.json
    # print(users)
    user = User.query.filter(User.email == email).one()
    # print(user.first_name)
    if user:
        user.first_name = users['first_name']
        user.last_name = users['last_name']
        # user.image = users['image']
        user.email = users['email']
        # user.password = data['password']
        db.session.commit()
        return {'user': user.as_dict()}
    # except AssertionError as message:
    #     print(str(message))
    else: 
        return jsonify(message="check your entries"), 400

@bp.route('/visits/<string:email>/<int:typeId>')
def user_visits(email, typeId):
    user = User.query.filter(User.email == email).one()
    # pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    # pointsofinterestbytype = [point.as_dict() for point in pointsofinterestbytype]
    # return {'pointsofinterest': pointsofinterestbytype}
    print(user.visits)
    # return {"visits": [v.as_dict() for v in user.visits]} 
    res = [{**visit.as_dict(), **{"pointsofinterest": visit.pointofinterest.as_dict()}} \
        for visit in user.visits if visit.pointofinterest.type_id == typeId]
    return {"visits": res}


@bp.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(Configuration.S3_BUCKET)
    summaries = my_bucket.objects.all()
    for o in summaries:
        print(o.key)
    return {"message": "bucket printed successfully"}, 200