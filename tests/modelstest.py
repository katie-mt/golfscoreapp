from app import db, app
from main import *
'''This file is meant to serve as a reference as to how to add objects to the db on your local machine after you have the mySQL database set up locally on your machine(with MAMP).
However if you run this file from the command line with \' $ python modelstest.py \' then it will reset your database and add four players, one tournament, one course, eighteen holes, and one score to it. '''

db.drop_all()
db.create_all()

'''This is how to add new players to the db
Constructor: Player(name) '''
db.session.add(Player('Player1'))
db.session.add(Player('Player2'))
db.session.add(Player('Player3'))
db.session.commit()

'''This is how you would add a new tournament to the db.
Constructor: Tournament(name)  '''
db.session.add(Tournament('Blue'))
db.session.commit()

'''This is how to add a new round to the db
Note that this will throw an exception if you reference a foreign key to a tournament that does not yet exist
Constuctor: Round(roundNumber, tournament_id)'''
db.session.add(Round(1,1))
db.session.commit()

'''This is how to add a Course to the db.
Constructor = Course(name)'''

db.session.add(Course('Brooke Woods'))
db.session.commit()

'''This is how to add a new hole to the db'''
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

'''This is how to add a new score to the db.
Note that this will throw an exception if you reference foreign keys that do not yet exist e.g... (round_id, hole_id, player_id) which is why this is placed last.
Constructor: Score(round_id, hole_id, player_id, score) '''
db.session.add(Score(1,1,1,5))
db.session.commit()
