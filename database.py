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

    # universities
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
    # states 
    point21 = PointOfInterest(
        title="Alabama",
        state='AL',
        lat="32.3773826",
        lng="-86.3026583",
        type_id=2
    )
    point22 = PointOfInterest(
        title="Alaska",
        state='AK',
        lat="58.3021115",
        lng="-134.4125825",
        type_id=2
    )
    point23 = PointOfInterest(
        title="Arizona",
        state='AZ',
        lat="33.4481099",
        lng="-112.0990525",
        type_id=2
    )
    point24 = PointOfInterest(
        title="Arkansas",
        state='AR',
        lat="34.7465139",
        lng="-92.2912489",
        type_id=2
    )
    point25 = PointOfInterest(
        title="California",
        state='CA',
        lat="38.5762624",
        lng="-121.4941635",
        type_id=2
    )
    point26 = PointOfInterest(
        title="Colorado",
        state='CO',
        lat="39.7393292",
        lng="-104.9870009",
        type_id=2
    )
    point27 = PointOfInterest(
        title="Connecticut",
        state='CT',
        lat="41.7640086",
        lng="-72.6881838",
        type_id=2
    )
    point28 = PointOfInterest(
        title="Delaware",
        state='DE',
        lat="39.1572789",
        lng="-75.5218064",
        type_id=2
    )
    # point29 = PointOfInterest(
    #     title="District of Columbia",
    #     state='DC',
    #     lat="41.8267718",
    #     lng="-71.404736",
    #     type_id=3
    # )
    point30 = PointOfInterest(
        title="Florida",
        state='FL',
        lat="30.4380644",
        lng="-84.2842649",
        type_id=2
    )
    point31 = PointOfInterest(
        title="Georgia",
        state='GA',
        lat="33.7488311",
        lng="-84.3902805",
        type_id=2
    )
    point32 = PointOfInterest(
        title="Hawai'i",
        state='HI',
        lat="21.3074777",
        lng="-157.8596091",
        type_id=2
    )
    point33 = PointOfInterest(
        title="Idaho",
        state='ID',
        lat="43.6178255",
        lng="-116.2017125",
        type_id=2
    )
    point34 = PointOfInterest(
        title="Illinois",
        state='IL',
        lat="39.7984664",
        lng="-89.6575816",
        type_id=2
    )
    point35 = PointOfInterest(
        title="Indiana",
        state='IN',
        lat="39.7687147",
        lng="-86.1650502",
        type_id=2
    )
    point36 = PointOfInterest(
        title="Iowa",
        state='IA',
        lat="41.5912062",
        lng="-93.6058329",
        type_id=2
    )
    point37 = PointOfInterest(
        title="Kansas",
        state='KS',
        lat="39.0481574",
        lng="-95.6802534",
        type_id=2
    )
    point38 = PointOfInterest(
        title="Kentucky",
        state='KY',
        lat="38.186757",
        lng="-84.8774912",
        type_id=2
    )
    point39 = PointOfInterest(
        title="Louisiana",
        state='LA',
        lat="30.4571235",
        lng="-91.1896261",
        type_id=2
    )
    point40 = PointOfInterest(
        title="Maine",
        state='ME',
        lat="44.3071776",
        lng="-69.7840212",
        type_id=2
    )
    point41 = PointOfInterest(
        title="Maryland",
        state='MD',
        lat="38.9789133",
        lng="-76.4932653",
        type_id=2
    )
    point42 = PointOfInterest(
        title="Massachusetts",
        state='MA',
        lat="42.3587811",
        lng="-71.404736",
        type_id=2
    )
    point43 = PointOfInterest(
        title="Michigan",
        state='MI',
        lat="42.7336313",
        lng="-84.5575884",
        type_id=2
    )
    point44 = PointOfInterest(
        title="Minnesota",
        state='MN',
        lat="44.9551538",
        lng="-93.104427",
        type_id=2
    )
    point45 = PointOfInterest(
        title="Mississippi",
        state='MS',
        lat="32.3038128",
        lng="-90.1842622",
        type_id=2
    )
    point46 = PointOfInterest(
        title="Missouri",
        state='MO',
        lat="38.579232",
        lng="-92.1751629",
        type_id=2
    )
    point47 = PointOfInterest(
        title="Montana",
        state='MT',
        lat="46.5855856",
        lng="-112.0199645",
        type_id=2
    )
    point48 = PointOfInterest(
        title="Nebraska",
        state='NE',
        lat="40.808074",
        lng="-96.7019318",
        type_id=2
    )
    point49 = PointOfInterest(
        title="Nevada",
        state='NV',
        lat="39.1639501",
        lng="-119.768317",
        type_id=2
    )
    point50 = PointOfInterest(
        title="New Hampshire",
        state='NH',
        lat="43.2069331",
        lng="-71.5402998",
        type_id=2
    )
    point51 = PointOfInterest(
        title="New Jersey",
        state='NJ',
        lat="40.2201753",
        lng="-74.772337",
        type_id=2
    )
    point52 = PointOfInterest(
        title="New Mexico",
        state='NM',
        lat="35.6822703",
        lng="-105.9418001",
        type_id=2
    )
    point53 = PointOfInterest(
        title="New York",
        state='NY',
        lat="42.6527759",
        lng="-73.7594328",
        type_id=2
    )
    point54 = PointOfInterest(
        title="North Carolina",
        state='NC',
        lat="35.7803627",
        lng="-78.6413231",
        type_id=2
    )
    point55 = PointOfInterest(
        title="North Dakota",
        state='ND',
        lat="46.820868",
        lng="-100.7849703",
        type_id=2
    )
    point56 = PointOfInterest(
        title="Ohio",
        state='OH',
        lat="39.9613908",
        lng="-83.0012949",
        type_id=2
    )
    point57 = PointOfInterest(
        title="Oklahoma",
        state='OK',
        lat="35.4957577",
        lng="-97.506149",
        type_id=2
    )
    point58 = PointOfInterest(
        title="Oregon",
        state='OR',
        lat="44.9393564",
        lng="-123.0323891",
        type_id=2
    )
    point59 = PointOfInterest(
        title="Pennsylvania",
        state='PA',
        lat="40.2642914",
        lng="-76.8861527",
        type_id=2
    )
    point60 = PointOfInterest(
        title="Rhode Island",
        state='RI',
        lat="41.8311369",
        lng="-71.416387",
        type_id=2
    )
    point61 = PointOfInterest(
        title="South Carolina",
        state='SC',
        lat="34.0003299",
        lng="-81.0353098",
        type_id=2
    )
    point62 = PointOfInterest(
        title="South Dakota",
        state='SD',
        lat="44.3671444",
        lng="-100.3485626",
        type_id=2
    )
    point63 = PointOfInterest(
        title="Tennessee",
        state='TN',
        lat="36.1658028",
        lng="-86.7864215",
        type_id=2
    )
    point64 = PointOfInterest(
        title="Texas",
        state='TX',
        lat="30.2746698",
        lng="-97.7425445",
        type_id=2
    )
    point65 = PointOfInterest(
        title="Utah",
        state='UT',
        lat="40.7774116",
        lng="-111.8903713",
        type_id=2
    )
    point66 = PointOfInterest(
        title="Vermont",
        state='VT',
        lat="44.2625754",
        lng="-72.5827215",
        type_id=2
    )
    point67 = PointOfInterest(
        title="Virginia",
        state='VA',
        lat="37.538816",
        lng="-77.4357889",
        type_id=2
    )
    point68 = PointOfInterest(
        title="Washington",
        state='WA',
        lat="47.0359458",
        lng="-122.9066392",
        type_id=2
    )
    point69 = PointOfInterest(
        title="West Virginia",
        state='WA',
        lat="38.336362",
        lng="-81.6143499",
        type_id=2
    )
    point70 = PointOfInterest(
        title="Wisconsin",
        state='WI',
        lat="43.0747349",
        lng="-89.3862353",
        type_id=2
    )
    point71 = PointOfInterest(
        title="Wyoming",
        state='WY',
        lat="41.1402745",
        lng="-104.8225553",
        type_id=2
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
    db.session.add(point21)
    db.session.add(point22)
    db.session.add(point23)
    db.session.add(point24)
    db.session.add(point25)
    db.session.add(point26)
    db.session.add(point27)
    db.session.add(point28)
    # db.session.add(point29)
    db.session.add(point30)
    db.session.add(point31)
    db.session.add(point32)
    db.session.add(point33)
    db.session.add(point34)
    db.session.add(point35)
    db.session.add(point36)
    db.session.add(point37)
    db.session.add(point38)
    db.session.add(point39)
    db.session.add(point40)
    db.session.add(point41)
    db.session.add(point42)
    db.session.add(point43)
    db.session.add(point44)
    db.session.add(point45)
    db.session.add(point46)
    db.session.add(point47)
    db.session.add(point48)
    db.session.add(point49)
    db.session.add(point50)
    db.session.add(point51)
    db.session.add(point52)
    db.session.add(point53)
    db.session.add(point54)
    db.session.add(point55)
    db.session.add(point56)
    db.session.add(point57)
    db.session.add(point58)
    db.session.add(point59)
    db.session.add(point60)
    db.session.add(point61)
    db.session.add(point62)
    db.session.add(point63)
    db.session.add(point64)
    db.session.add(point65)
    db.session.add(point66)
    db.session.add(point67)
    db.session.add(point68)
    db.session.add(point69)
    db.session.add(point70)
    db.session.add(point71)
    db.session.commit()