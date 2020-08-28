from flask import Blueprint, request, jsonify
import json
from flask_cors import cross_origin
from ..models import db, Visit, User
# from ..config import Configuration

bp = Blueprint("visits", __name__, url_prefix="/api/visits")


@bp.route('/<int:typeId>')
def visits(typeId):
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    pointsofinterestbytype = [point.visit.as_dict() for point in pointsofinterestbytype]
    return {'pointsofinterest': pointsofinterestbytype}

@bp.route('/entry', methods=['POST'])
# @cross_origin()
def log_entry():
    data = json.loads(request.get_data().decode('UTF-8'))
    email = data["email"]
    user = User.query.filter_by(email=email).first()
    # print(user)
    user_id = user.id
    images = data['images']
    rating = data['rating']
    start_date_visited = data['visitDate']
    pointsOfInterest_id = data['point']
    visit = Visit(user_id=user_id, images=images, rating=rating, start_date_visited=start_date_visited, pointsOfInterest_id = pointsOfInterest_id)
    db.session.add(visit)
    db.session.commit()
    return {'visit': visit.as_dict()}

