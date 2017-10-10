from app import db

'''In java, classes usually go in their own file but for some reason the norm in python is to throw them
all into one file called models so here they are...'''

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    rounds = db.relationship('Round', backref='owner')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tournament %r' % self.name


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer,db.ForeignKey('round.id'))
    hole_id = db.Column(db.Integer, db.ForeignKey('hole.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    score = db.Column(db.Integer)

    def __init__(self, round_id, hole_id, player_id, score):
        self.round_id = round_id
        self.hole_id = hole_id
        self.player_id = player_id
        self.score = score

    def __repr__(self):
        return '<Score %d' % self.score


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    db.relationship('Hole', backref = 'owner')


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Course %r' % self.name

class Hole(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    par = db.Column(db.Integer)
    owner = db.Column(db.Integer, db.ForeignKey('course.id'))
    scores = db.relationship('Score', backref='hole')


    def __init__(self, owner, par):
        self.owner = owner
        self.par = par

    def __repr__(self):
        return 'Hole %d' % self.id


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    scores = db.relationship('Score', backref='player')


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Player %r>' % self.name

class Round(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    round_number = db.Column(db.Integer)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
    scores = db.relationship('Score', backref='round')

    def __init__(self, round_number, tournament_id):
        self.round_number = round_number
        self.tournament_id = tournament_id

    def __repr__(self):
        return 'Round %d' % self.roundNum
