import os 

class Configuration: 
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://travel_app_user:travel@localhost/travel_app_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False