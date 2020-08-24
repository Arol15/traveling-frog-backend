from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
load_dotenv()

from app import app, db
from app.models import (
    User, PlaceType, PointOfInterest)

with app.app_context():
    db.drop_all()
    db.create_all()

    # 2 users - demo 
    # 3 collections: National Parks, State of the U.S., Top U.S. Universities
    # Points of interests 

    user1 = User(
        first_name='Lora',
        last_name='Palmer',
        hashed_password=generate_password_hash('123456'),
        email='lora@me.com',

    )
    demoUser = User(
        first_name='Frog',
        last_name='Traveling',
        hashed_password=generate_password_hash('123456'),
        email='test@gmail.com',
        image="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSi4_H8CA9FRnWDyAShbVpHXMadRHX3VVxYGQ&usqp=CAU"
    )

    collection1 = PlaceType(
       type="U.S. National Parks",
       image="https://i.pinimg.com/originals/6f/cd/66/6fcd66a405936566e17938daf8c82cb1.jpg"
    )

    collection2 = PlaceType(
        type="States of the U.S.", 
        image="https://i.pinimg.com/originals/7d/ff/c1/7dffc1cf55a606bcfeba7926a38d96ae.jpg"  
    )

    collection3 = PlaceType(
        type="Top U.S. Universities",
        image="https://cdn.britannica.com/25/121725-004-49025455.jpg"
    )

    point1 = PointOfInterest(
        title="Yellowstone",
        state='Utah',
        lat="44.423691",
        lng="-110.588516",
        type_id=1
    )

    # point2 = PointOfInterest(
    #     title="Grand Canyon",
    #     state='Arizona',
    #     lat="",
    #     lng=""
    # )
    # point3 = PointOfInterest(
    #     title="Everglades",
    #     state='Florida',
    #     lat="",
    #     lng=""
    # )
    # point4 = PointOfInterest(
    #     title="Yosemite",
    #     state='California',
    #     lat="",
    #     lng=""
    # )
    # point5 = PointOfInterest(
    #     title="Zion",
    #     state='Arizona',
    #     lat="",
    #     lng=""
    # )
    # point6 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point7 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point8 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point9 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point10 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point11 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point12 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point13 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point14 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )
    # point15 = PointOfInterest(
    #     title="",
    #     state='',
    #     lat="",
    #     lng=""
    # )


    db.session.add(user1)
    db.session.add(demoUser)
    db.session.add(collection1)
    db.session.add(collection2)
    db.session.add(collection3)
    db.session.add(point1)
    db.session.commit()