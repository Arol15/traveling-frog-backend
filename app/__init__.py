from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

from app.config import Configuration
from app.models import db

app = Flask(__name__)

app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

