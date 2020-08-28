from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
import boto3

from app.config import Configuration
from app.routes import users, session, collections, visits, pointsofinterest
from app.models import db

s3_resource = boto3.resource(
    "s3", 
    aws_access_key_id=Configuration.S3_KEY,
    aws_secret_access_key=Configuration.S3_SECRET_ACCESS_KEY
)

app = Flask(__name__)
CORS(app, support_credentials=True)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users.bp)
app.register_blueprint(session.bp)
app.register_blueprint(collections.bp)
app.register_blueprint(pointsofinterest.bp)
app.register_blueprint(visits.bp)
