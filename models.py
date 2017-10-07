from app import db

'''In java, classes usually go in their own file but for some reason the norm in python is to throw them
all into one file called models so here they are...'''

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    round = db.relationship('Round', backref='course')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Course %r' % self.name

class Hole(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    par = db.Column(db.Integer)

    def __init__(self,par):
        self.par = par

    def __repr__(self):
        return 'Hole %d' % self.id


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    round = db.relationship('Round', backref = 'player')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Player %r>' % self.name

class Round(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    roundNum = db.Column(db.Integer)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    player_one = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_two = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_three = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_four = db.Column(db.Integer, db.ForeignKey('player.id'))




    def __init__(self, roundNum, player_one, player_two, player_three, player_four):
        self.roundNum = roundNum
        self.player_one = player_one
        self.player_two = player_two
        self.player_three = player_three
        self.player_four = player_four

    def __repr__(self):
        return 'Round %d' % self.roundNum
