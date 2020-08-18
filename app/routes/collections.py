from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from ..models import db, PlaceType
from ..auth import require_auth

bp = Blueprint("placetypes", __name__, url_prefix='/api/collections')

@bp.route('') #fetch all collections
# @require_auth
def collections(): 
    collections = PlaceType.query.all()
    collections = [collection.as_dict() for collection in collections]
    return jsonify(collections)
    # return {"collections": collections}