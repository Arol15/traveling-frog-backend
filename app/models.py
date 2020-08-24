from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import re
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class MixinAsDict:
    def as_dict(self, skip=["hashed_password"]):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in skip}

class User(MixinAsDict, db.Model): 
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String, default="https://miro.medium.com/max/720/1*W35QUSvGpcLuxPo3SRTH4w.png") # add later
    hashed_password = db.Column(db.String(100), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    visits = db.relationship('Visit', backref='user', lazy=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_valid_email(self, email):
        return not re.match("[^@]+@[^@]+\.[^@]+", email)

    def __repr__(self):
        return f"User with {self.email} and {self.password}"

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "image": self.image,
        }

# TODO: def to_dictionary(self):

class PointOfInterest(MixinAsDict, db.Model):
    __tablename__ = 'pointsofinterest'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(300))
    city = db.Column(db.String(50))
    state = db.Column(db.String(20))
    country = db.Column(db.String(50))
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    private = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('placetypes.id'), nullable=False)

    placetype = db.relationship("PlaceType", backref="pointofinterest", lazy=True)
    # visit = db.relationship("Visit", backref='pointofinterest', lazy=True)

    # def to_dict(): 
    #     return {
    #         "title": self.title,
    #         "address": self.address,
    #         "city": self.city,
    #         "state": self.state,
    #         "country": self.country,
    #         "lat": self.lat,
    #         "lng": self.lng,
    #         "visited": False,
    #     }

    def __repr__(self):
        return f'PointOfInterest: {self.title}, {self.address}, {self.city}, {self.state}, {self.country}'


class PlaceType(MixinAsDict, db.Model):
    __tablename__ = 'placetypes'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False, unique=True)
    image = db.Column(db.String)


class Visit(MixinAsDict, db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    pointsOfInterest_id = db.Column(db.Integer, db.ForeignKey('pointsofinterest.id'), nullable=False)
    start_date_visited = db.Column(db.DateTime, nullable=False)
    end_date_visited = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    images = db.Column(db.ARRAY(db.String(255)))
    rating = db.Column(db.Integer, default=0)

    # user = db.relationship('User', backref='visits', lazy=True)
    pointofinterest = db.relationship('PointOfInterest', backref='visit', lazy=True)


    def __repr__(self):
        return f'Visit: {self.start_date_visited}, {self.rating}'


