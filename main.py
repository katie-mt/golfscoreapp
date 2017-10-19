from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Round_Player_Table, Course, Hole, Score


@app.route("/")
def index():
   encoded_error = request.args.get("error")
   return redirect('/courses')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    elif request.method == 'POST':
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
    session.clear()
    print(session.keys())
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



'''The following route pulls all the courses from the DB and puts them into
the courses variable which is sent to the template where a loop can pull 
the course name'''
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

@app.route('/process_players', methods=['POST', 'GET'])
def process_players():
    if request.method == 'POST':
        player_1_Name = request.form['player1']
        db.session.add(Player(player_1_Name))
        player_2_Name = request.form['player2']
        db.session.add(Player(player_2_Name))
        player_3_Name = request.form['player3']
        db.session.add(Player(player_3_Name))
        player_4_Name = request.form['player4']
        db.session.add(Player(player_4_Name))
        db.session.commit()
        session['player_1_Name'] = player_1_Name
        session['player_2_Name'] = player_2_Name
        session['player_3_Name'] = player_3_Name
        session['player_4_Name'] = player_4_Name
        return redirect('/score_input')




@app.route('/score_input', methods=['POST', 'GET'])
def score_input():
    this_Rounds_Players = []
    this_Rounds_Players += Player.query.filter_by(name = session['player_1_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_2_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_3_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_4_Name'])

    if 'hole_num' not in session:
        session['hole_num'] = 1
    if 'round_num' not in session:
        session['round_num'] = 1
    return render_template('score_input.html', players=this_Rounds_Players, hole_num=session['hole_num'], round_num=session['round_num'])



@app.route('/process_score', methods=['POST', 'GET'])
def process_score():
    tournament_id = 1
    if session['hole_num'] >= 18:
        session['round_num'] += 1
        session['hole_num'] = 1
        db.session.add(Round(session['round_num'],tournament_id))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=1))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=2))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=3))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=4))
        return redirect('/leaderboard')

    player_1_Score = int(request.form['player_1_score'])
    player_2_Score = int(request.form['player_2_score'])
    player_3_Score = int(request.form['player_3_score'])
    player_4_Score = int(request.form['player_4_score'])
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], player_id=1, score=player_1_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], player_id=2, score=player_2_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], player_id=3, score=player_3_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], player_id=4, score=player_4_Score))
    session['hole_num'] += 1
    db.session.commit()
    return redirect('/score_input')




def logged_in_user():
    owner = User.query.filter_by(email=session['user']).first()
    return owner

endpoints_without_login = ['signup' ,'leaderboard', 'signin']

@app.before_request
def require_login():
    if not ('user' in session or request.endpoint in endpoints_without_login):
        return redirect("/signin")

@app.route("/scoreinput", methods=['POST', 'GET'])
def input_score():
    User.id = User.query.filter_by(id=id)
    if request.method == 'POST':


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'
        score1 = request.form['score1']
        score2 = request.form['score2']
        score3 = request.form['score3']
        score4 = request.form['score4']
        Tournament(player_id)score()

        round_id = Round.query.filter_by(round_id=round_id)
        hole_id = Hole.query.filter_by(hole_id=hole_id)
        player_id = Player.query.filter_by(player_id=player_id)
        scoreinput = Score(id=id, round_id=round_id, hole_id=hold_id, player_id=player_id, score=score)
        db.session.add(scoreinput)
        hole_id = hole_id +1
        if hole_id > 18:
            round_id = round_id +1
            hole_id == 1
            db.session.add(round_id)
        db.session.add(hole_id)
        db.session.commit()
        """Add User session validation """
        return redirect("/score-input.html", scoreinput=scoreinput, hole_id=hole_id, round_id=round_id)
    else:
        @app.before_request
        def require_login():
            if not ('user' in session or request.endpoint in endpoints_without_login):
                
        return render_template("score-input.html", user=user, round_id=round_id, hole_id=hole_id, player_id=player_id, score=score)
    """will i get a bug on the first input prompt because vars will be empty?"""

@app.route("/leaderboard", methods=['GET'])
"""generating the data for every players score. assuming a for loop will be used in the template to list every players score"""
    if request.method == 'GET':
        players[] = Player.query.filter_by(score=score)
        round_id = Round.query.filter_by(round_id=round_id)
        """all_scores = Score.query.all(score=score)"""
        """player_id = User.query.all(player_id=player_id)"""
        """score_db = Score(id=id, round_id=round_id, hole_id=hold_id, player_id=player_id, score=score)"""
        return render_template("leaderboard.html," user=user, players=players, score=score, round_id=round_id)


if __name__ == '__main__':
    app.run()
