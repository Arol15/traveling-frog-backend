import os 

class Configuration: 
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL") or "postgresql://travel_app_user:travel@localhost/travel_app_db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get("SECRET_KEY")
    S3_BUCKET=os.environ.get("S3_BUCKET")
    S3_KEY=os.environ.get("S3_KEY")
    S3_SECRET_ACCESS_KEY=os.environ.get("S3_SECRET_ACCESS_KEY")
