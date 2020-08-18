from flask import Blueprint, request, jsonify
from ..models import db, PointOfInterest

bp = Blueprint("pointsofinterest", __name__, url_prefix="/api/pointsofinterest")


@bp.route('/<int:typeId>')
def pointsofinterest(typeId):
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    pointsofinterestbytype = [point.as_dict() for point in pointsofinterestbytype]
    return {'pointsofinterest': pointsofinterestbytype}