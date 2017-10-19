from app import db, app
from main import *
'''This file is meant to serve as a reference as to how to add objects to the db on your local machine after you have the mySQL database set up locally on your machine(with MAMP).
However if you run this file from the command line with \' $ python modelstest.py \' then it will reset your database and add four players, one tournament, one course, eighteen holes, and one score to it. '''

db.drop_all()
db.create_all()

'''This is how to add new users to the db
Constructor: User(username, email, password) '''

db.session.add(User('golfguy','golfguy@gmail.com','golfislife'))
db.session.commit()

'''This is how you would add a new tournament to the db.
Constructor: Tournament(owner_id, name)  '''
db.session.add(Tournament(1,"Blue"))
db.session.commit()

'''This is how to add a Course to the db.
Constructor = Course(name)'''

db.session.add(Course('Brooke Woods'))
db.session.add(Course('Emerald Valley'))
db.session.add(Course('Broadmoore West Course'))
db.session.commit()


'''This is how to add a new hole to the db
Constructor: Hole(owner_id, par)'''
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
