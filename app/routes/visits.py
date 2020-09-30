from flask import Blueprint, request, jsonify
import json
from flask_cors import cross_origin
from ..models import db, Visit, User
from ..config import Configuration
import boto3

bp = Blueprint("visits", __name__, url_prefix="/api/visits")


@bp.route('/<int:typeId>')
def visits(typeId):
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    pointsofinterestbytype = [point.visit.as_dict() for point in pointsofinterestbytype]
    return {'pointsofinterest': pointsofinterestbytype}

# @bp.route('/entry', methods=['POST'])
# # @cross_origin()
# def log_entry():
#     data = json.loads(request.get_data().decode('UTF-8'))
#     email = data["email"]
#     user = User.query.filter_by(email=email).first()
#     # print(user)
#     user_id = user.id
#     images = data['images']
#     rating = data['rating']
#     start_date_visited = data['visitDate']
#     pointsOfInterest_id = data['point']
#     visit = Visit(user_id=user_id, images=images, rating=rating, start_date_visited=start_date_visited, pointsOfInterest_id = pointsOfInterest_id)
#     db.session.add(visit)
#     db.session.commit()
#     return {'visit': visit.as_dict()}


@bp.route('/entry', methods=['POST'])
# @cross_origin()
def log_entry():
    data = request.form
    print(data)

    file = request.files['image']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(Configuration.S3_BUCKET_NAME)
    my_bucket.Object(file.filename).put(Body=file, ACL='public-read')

    email = data["email"]
    user = User.query.filter_by(email=email).first()

    new_visit = {
        "user_id": user.id, 
        "image": f'https://traveling-frog-app.s3.us-east-2.amazonaws.com/{my_bucket.Object(file.filename).key}',
        "rating": data['rating'], 
        "start_date_visited": data['visitDate'],
        "pointsOfInterest_id": data['point']
    }

    visit = Visit(**new_visit)
    print(visit.as_dict())
    db.session.add(visit)
    db.session.commit()
    return {'visit': visit.as_dict()}

    # data = json.loads(request.get_data().decode('UTF-8'))
    # email = data["email"]
    # user = User.query.filter_by(email=email).first()
    # # print(user)
    # user_id = user.id
    # images = data['images']
    # rating = data['rating']
    # start_date_visited = data['visitDate']
    # pointsOfInterest_id = data['point']
    # visit = Visit(user_id=user_id, images=images, rating=rating, start_date_visited=start_date_visited, pointsOfInterest_id = pointsOfInterest_id)
    # db.session.add(visit)
    # db.session.commit()
    # return {'visit': visit.as_dict()}

