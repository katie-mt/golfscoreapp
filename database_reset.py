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


db.session.add(Hole(1,4,1))
db.session.add(Hole(1,5,2))
db.session.add(Hole(1,4,3))
db.session.add(Hole(1,3,4))
db.session.add(Hole(1,5,5))
db.session.add(Hole(1,6,6))
db.session.add(Hole(1,4,7))
db.session.add(Hole(1,4,8))
db.session.add(Hole(1,5,9))
db.session.add(Hole(1,7,10))
db.session.add(Hole(1,6,11))
db.session.add(Hole(1,4,12))
db.session.add(Hole(1,5,13))
db.session.add(Hole(1,5,14))
db.session.add(Hole(1,6,15))
db.session.add(Hole(1,4,16))
db.session.add(Hole(1,7,17))
db.session.add(Hole(1,4,18))

db.session.commit()
