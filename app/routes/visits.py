from flask import Blueprint, request, jsonify
from ..models import db, Visit

bp = Blueprint("visits", __name__, url_prefix="/api/")


@bp.route('/<int:typeId>')
def visits(typeId):
    pointsofinterestbytype = PointOfInterest.query.filter(PointOfInterest.type_id == typeId).all()
    pointsofinterestbytype = [point.visit.as_dict() for point in pointsofinterestbytype]
    return {'pointsofinterest': pointsofinterestbytype}

