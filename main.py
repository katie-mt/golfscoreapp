from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Course, Hole, Score


@app.route("/")
def index():
   encoded_error = request.args.get("error")
   return redirect('/courses')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        print('am I getting here?')
        return render_template('signin.html')
    elif request.method == 'POST':
        print('what about here?')
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email)
        if users.count() == 1:
            user = users.first()
            if user.password == password:
                session['user'] = user.email
                flash('welcome back, ' + user.email)
                return redirect("/")
        flash('bad username or password')
        '''have it redirect to courses page until other controllers are implemented'''
        return redirect("/courses")

@app.route('/logout', methods=['POST'])
def logout():
    del session['user']
    return redirect('/')


@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        email_db_count = User.query.filter_by(email=email).count()
        if email_db_count > 0:
            flash('yikes! ' + email + ' is already taken')
            return redirect('/signup')
        if password != verify:
            flash('passwords did not match')
            return redirect('/signup')
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        session['user'] = user.email
        return redirect("/")
    else:
        return render_template('signup.html', title='Sign up!')


@app.route("/courses")
def list_courses():
    courses = Course.query.all()
    return render_template("list_courses.html", courses=courses)


@app.route("/initiate_tournament", methods=['GET', 'POST'])
def initiate_tournament():
    if request.method == 'GET':
        return render_template('tournament_initiation.html', title='Start A Tournament')
    elif request.method == 'POST':
        tournament_course = request.form['course']
        return render_template('tournament_initiation.html', title='Starting Tournament', course=tournament_course)

@app.route('/score_input', methods=['POST', 'GET'])
def score_input():
    if request.method == 'POST':
        player_1 = request.form['player1']
        db.session.add(Player(player_1))
        player_2 = request.form['player2']
        db.session.add(Player(player_2))
        player_3 = request.form['player3']
        db.session.add(Player(player_3))
        player_4 = request.form['player4']
        db.session.add(Player(player_4))
        db.session.commit()

        this_Rounds_Players = []
        this_Rounds_Players += Player.query.filter_by(name = player_1)
        this_Rounds_Players += Player.query.filter_by(name = player_2)
        this_Rounds_Players += Player.query.filter_by(name = player_3)
        this_Rounds_Players += Player.query.filter_by(name = player_4)

        return render_template('score_input.html', players=this_Rounds_Players)

'''@app.route('handle_score', methods=['POST', 'GET'])
def handle_score():
    if request.method == 'POST':

'''


def logged_in_user():
    owner = User.query.filter_by(email=session['user']).first()
    return owner

endpoints_without_login = ['signup' ,'leaderboard', 'signin']

@app.before_request
def require_login():
    if not ('user' in session or request.endpoint in endpoints_without_login):
        return redirect("/signin")



app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == '__main__':
    app.run()
