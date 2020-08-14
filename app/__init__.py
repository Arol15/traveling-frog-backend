from flask import Flask
# from flask_restx import Api
from flask_migrate import Migrate
from flask_cors import CORS

from app.config import Configuration
from app.routes import users, session, placetypes, visits, pointsofinterest
from app.models import db

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users.bp)
app.register_blueprint(session.bp)
# app.register_blueprint(placetypes.py)
# app.register_blueprint(pointsofinterest.py)
# app.register_blueprint(visits)
