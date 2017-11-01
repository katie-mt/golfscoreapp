from app import db, app
from main import *
'''This file is meant to reset the database with some data hard coded in(functionality can be added later)'''

db.drop_all()
db.create_all()



db.session.add(User('golfguy','golfguy@gmail.com','golfislife'))
db.session.commit()



db.session.add(Course('Brooke Woods'))
db.session.add(Course('Emerald Valley'))
db.session.add(Course('Broadmoore West Course'))
db.session.commit()


db.session.add(Hole(1,4))
db.session.add(Hole(1,5))
db.session.add(Hole(1,4))
db.session.add(Hole(1,3))
db.session.add(Hole(1,5))
db.session.add(Hole(1,6))
db.session.add(Hole(1,4))
db.session.add(Hole(1,4))
db.session.add(Hole(1,5))
db.session.add(Hole(1,7))
db.session.add(Hole(1,6))
db.session.add(Hole(1,4))
db.session.add(Hole(1,5))
db.session.add(Hole(1,5))
db.session.add(Hole(1,6))
db.session.add(Hole(1,4))
db.session.add(Hole(1,7))
db.session.add(Hole(1,4))

db.session.commit()
