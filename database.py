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
        image="https://i.redd.it/30363cj9nsl11.jpg"  
    )

    collection3 = PlaceType(
        type="U.S. Universities",
        image="https://www.timeshighereducation.com/sites/default/files/stanford-university-best-universities-in-the-united-states-2016.jpg"
    )

    point1 = PointOfInterest(
        title="Yellowstone",
        state='WY',
        lat="44.291842",
        lng="-110.001380",
        type_id=1
    )

    point2 = PointOfInterest(
        title="Grand Canyon",
        state='AZ',
        lat="36.056198",
        lng="-112.125198",
        type_id=1
    )
    point3 = PointOfInterest(
        title="Everglades",
        state='FL',
        lat="25.2866155",
        lng=" -80.8986509",
        type_id=1
    )
    point4 = PointOfInterest(
        title="Yosemite",
        state='CA',
        lat="37.9083432",
        lng="-119.539726",
        type_id=1
    )
    point5 = PointOfInterest(
        title="Zion",
        state='UT',
        lat="37.3223063",
        lng="-113.324112",
        type_id=1
    )
    point6 = PointOfInterest(
        title="Grand Teton",
        state='WY',
        lat="44.6021658",
        lng="-112.1245949",
        type_id=1
    )
    point7 = PointOfInterest(
        title="Mount Rainer",
        state='WA',
        lat="46.9421834",
        lng="-122.1588316",
        type_id=1
    )

    point8 = PointOfInterest(
        title="Hawaii Volcanoes",
        state='HI',
        lat="19.3833748",
        lng="-155.2175571",
        type_id=1
    )
    point9 = PointOfInterest(
        title="Kenai Fjords",
        state='AK',
        lat="59.9902432",
        lng="-151.5459454",
        type_id=1
    )
    point10 = PointOfInterest(
        title="Rocky Mountain",
        state='CO',
        lat="40.3427932",
        lng="-147.3561518",
        type_id=1
    )
    point11 = PointOfInterest(
        title="University of Pennsylvania",
        state='PA',
        lat="39.9522188",
        lng="-75.1954024",
        type_id=3
    )

    point12 = PointOfInterest(
        title="Stanford University",
        state='CA',
        lat="37.4274745",
        lng="-122.1719077",
        type_id=3
    )
    point13 = PointOfInterest(
        title="Harvard University",
        state='MA',
        lat="42.5356105",
        lng="-71.0878922",
        type_id=3
    )
    point14 = PointOfInterest(
        title="Princeton University",
        state='NJ',
        lat="40.3430942",
        lng="-74.6572626",
        type_id=3
    )
    point15 = PointOfInterest(
        title="Yale University",
        state='CT',
        lat="41.4478783",
        lng="-73.3595062",
        type_id=3
    )
    point16 = PointOfInterest(
        title="Duke University",
        state='NC',
        lat="36.0014258",
        lng="-78.9404173",
        type_id=3
    )
    point17 = PointOfInterest(
        title="University of California, Berkeley",
        state='CA',
        lat="37.8718992",
        lng="-122.2607286",
        type_id=3
    )
    point18 = PointOfInterest(
        title="Massachusetts Institute of Technology",
        state='MA',
        lat="42.4599287",
        lng="-70.9951039",
        type_id=3
    )
    point19 = PointOfInterest(
        title="Columbia University",
        state='NY',
        lat="40.8075355",
        lng="-73.9647614",
        type_id=3
    )
    point20 = PointOfInterest(
        title="Brown University",
        state='RI',
        lat="41.8267718",
        lng="-71.404736",
        type_id=3
    )


    db.session.add(user1)
    db.session.add(demoUser)
    db.session.add(collection1)
    db.session.add(collection2)
    db.session.add(collection3)
    db.session.add(point1)
    db.session.add(point2)
    db.session.add(point3)
    db.session.add(point4)
    db.session.add(point5)
    db.session.add(point6)
    db.session.add(point7)
    db.session.add(point8)
    db.session.add(point9)
    db.session.add(point10)
    db.session.add(point11)
    db.session.add(point12)
    db.session.add(point13)
    db.session.add(point14)
    db.session.add(point15)
    db.session.add(point16)
    db.session.add(point17)
    db.session.add(point18)
    db.session.add(point19)
    db.session.add(point20)
    db.session.commit()