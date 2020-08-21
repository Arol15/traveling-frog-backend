from flask import Blueprint, request, jsonify
from ..models import db, PointOfInterest, User

bp = Blueprint("pointsofinterest", __name__, url_prefix="/api/pointsofinterest")


@bp.route('/<int:typeId>')
def pointsofinterest(typeId):
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    pointsofinterestbytype = [point.as_dict() for point in pointsofinterestbytype]
    return {'pointsofinterest': pointsofinterestbytype}

@bp.route('/<int:typeId>/<string:email>')
def pointsofinterestwithvisit(typeId, email):
    user = User.query.filter(User.email == email).one()
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    placesofinterestwithvisited = []

    for point in pointsofinterestbytype: 
        interest = {}
        interest["title"] = point.title
        interest["state"] = point.state
        interest["lat"] = point.lat
        interest["lng"] = point.lng
        interest["address"] = point.address
        interest["id"] = point.id
        interest['visited'] = False 
        for visit in user.visits: 
            if visit.pointofinterest.id == point.id:
                interest['visited'] = True
                interest["rating"] = visit.rating
                interest['images'] = visit.images
                interest['start_date_visited'] = visit.start_date_visited
                interest['end_date_visited'] = visit.end_date_visited
        placesofinterestwithvisited.append(interest)
    return {'pointsofinterest': placesofinterestwithvisited}




