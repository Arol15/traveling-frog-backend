from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import re
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model): 
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String, nullable=False, default="https://miro.medium.com/max/720/1*W35QUSvGpcLuxPo3SRTH4w.png") # add later
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
        return self.check_password_hash(self.password, password)

    def is_valid_email(self, email):
        return not re.match("[^@]+@[^@]+\.[^@]+", email)

    def __repr__(self):
        return f"User with {self.email} and {self.password}"

# TODO: def to_dictionary(self):

class PointOfInterest(db.Model):
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
    type_id = db.Column(db.Integer, db.ForeignKey('placetypes.id'), nullable=False)

    placetype = db.relationship("PlaceType", backref="pointofinterest", lazy=True)

    def __repr__(self):
        return f'PointOfInterest: {self.title}, {self.address}, {self.city}, {self.state}, {self.country}'


class PlaceType(db.Model):
    __tablename__ = 'placetypes'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False, unique=True)


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    pointsOfInterest_id = db.Column(db.Integer, db.ForeignKey('pointsofinterst.id'), nullable=False)
    start_date_visited = db.Column(db.DateTime, nullable=False)
    end_date_visited = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    images = db.Column(db.ARRAY(db.String(255)))
    rating = db.Column(db.Integer, default=0)

    # user = db.relationship('User', backref='visits', lazy=True)
    pointofinterest = db.relationship('PointOfInterest', backref='visit', lazy=True)


    def __repr__(self):
        return f'Visit: {self.start_date_visited}, {self.rating}'

