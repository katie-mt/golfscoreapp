from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Round_Player_Table, Course, Hole, Score
from sqlalchemy import desc

def logged_in_user_id():
    return User.query.filter_by(email=session['user']).first().id


@app.route("/")
def index():
   encoded_error = request.args.get("error")
   return redirect('/courses')

@app.route("/signin", methods=['GET', 'POST'])
def signin():#Accessible without logging in.
    if request.method == 'GET':#During a get request, display the blank signin template
        return render_template('signin.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        users = User.query.filter_by(email=email)
        if users.count() == 1:#Validate if user exsists in the database
            user = users.first()
            if user.password == password:
                session['user'] = user.email#Put user email into Session variable
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

@app.route("/signup", methods=['GET'])
def display_signup():#show signup blank signup template on from get request
    return render_template('signup.html', title='Sign Up!')

@app.route("/signup", methods=['POST'])
def validate_user():#Validate signup inputs and record errors if there are any.
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    verify = request.form['verify']
    email_db_count = User.query.filter_by(email=email).count()
    username_db_count = User.query.filter_by(username=username).count()
    user_error = ''
    password_error1 = ''
    password_error2 = ''
    email_error = ''

    if not " " in username:
        if username_db_count == 0:
            if len(username) < 3 or len(username) > 20:
                user_error = "Sliced it! User name must be between 3 and 20 characters with no spaces. Please try again."
        else:
            user_error = "Sliced it! User name is already taken. Please try again."
    else:
        user_error = "Sliced it! User name must be between 3 and 20 characters with no spaces. Please try again."

    if not " " in password:
        if len(password) < 3 or len(password) > 20:
            password_error1 = "Chunked it! Password must be between 3 and 20 characters with no spaces. Please try again."
    else:
        password_error1 = "Chunked it! Password must be between 3 and 20 characters with no spaces. Please try again."

    if password != verify:
        password_error2 = "Double Bogey! Passwords do not match."

    if not " " in email:
        if email_db_count == 0:
            if len(email) >= 3 and len(email) <= 30:
                if "@" in email and "." in email:
                    email_error = ''
                else:
                    email_error = "Shanked it! Email can be blank or must contain '@' and '.' to be valid. Please try again."
            else:
                email_error = "Shanked it! Email can be blank or must contain '@' and '.' to be valid. Please try again."
        else:
            email_error = "Shanked it! Email is already taken. Please try again."
    else:
        email_error = "Shanked it! Email can\'t be blank or must contain '@' and '.' to be valid. Please try again."

    if not user_error and not password_error1 and not password_error2 and not email_error:
        user = User(username=username, email=email, password=password)
        #When there is no error's present, log the user into the database and create a session variable with email
        db.session.add(user)
        db.session.commit()
        session['user'] = user.email
        return redirect('/')
    else:#When there are errors, display signup template with errors passed through using Jinja
        return render_template("signup.html", username=username, email=email,
    username_error=user_error, password_error1=password_error1,
    password_error2=password_error2, email_error=email_error)

@app.route("/courses")
def list_courses():#Queries the database for all Course names and passes them to template. Template loops and displays names.
    courses = Course.query.all()
    return render_template("list_courses.html", courses=courses)

@app.route("/initiate_tournament", methods=['POST'])#This route is only accessed through the post request from list_courses template
def initiate_tournament():

    tournament_course = request.form['course']#pulls name of course from list_courses template
    session['course'] = tournament_course#puts that course name in session variable with key 'course'
    course = Course.query.filter_by(name = tournament_course).first()#assigns course database object to variable via the course name
    course_id = course.id #assigns course ID from db to variable
    session['course_id'] = course_id #puts course ID varible into session with key 'course_id'
    return render_template('tournament_initiation.html', title='Starting Tournament', course=tournament_course)#sends course name to template using Jinja

@app.route('/process_players', methods=['POST'])
def process_players():#This method sets up players in the database so that their scores can be tracked
    #This adds a tournament to the database
    tournament_Name = request.form['tournament_name']#Sent via post from the initiate_tournament template
    tournament_Owner_Id = User.query.filter_by(email=session['user']).first().id#Uses the logged in user session to assign a owner ID
    db.session.add(Tournament(tournament_Owner_Id, tournament_Name))#Intatiates a tournament with ownerID and tournament name
    db.session.commit()#Confirms tournament intatiation
    session['tournament_Id'] = Tournament.query.filter_by(name=tournament_Name).first().id#Assigns tournemant ID to session variable with key 'tournament_ID'

    player_1_Name = request.form['player1']
    db.session.add(Player(player_1_Name,session['tournament_Id']))#Players are instatiated using player name from template POST request and tournament_ID session variable
    player_2_Name = request.form['player2']
    db.session.add(Player(player_2_Name,session['tournament_Id']))
    player_3_Name = request.form['player3']
    db.session.add(Player(player_3_Name,session['tournament_Id']))
    player_4_Name = request.form['player4']
    db.session.add(Player(player_4_Name,session['tournament_Id']))
    db.session.commit()
    #After players have been confirmed in the DB, their name is assigned into Session variables
    session['player_1_Name'] = player_1_Name
    session['player_2_Name'] = player_2_Name
    session['player_3_Name'] = player_3_Name
    session['player_4_Name'] = player_4_Name
    return redirect('/score_input')

@app.route('/score_input')#This route handles score input
def score_input():#this fills in a blank template with player,round,and par information for use in score inputs.
    this_Rounds_Players = []#create an empty list then add player names from session into the list
    this_Rounds_Players += Player.query.filter_by(name = session['player_1_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_2_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_3_Name'])
    this_Rounds_Players += Player.query.filter_by(name = session['player_4_Name'])
    if 'hole_num' not in session: #This tracks the current hole number being scored

    if request.method == 'GET':
        return render_template('tournament_initiation.html', title='Start A Tournament')
    elif request.method == 'POST':
        tournament_course = request.form['course']
        session['course'] = tournament_course
        course = Course.query.filter_by(name = tournament_course).first()
        course_id = course.id
        session['course_id'] = course_id
        return render_template('tournament_initiation.html', title='Starting Tournament', course=tournament_course)

@app.route('/process_players', methods=['POST', 'GET'])
def process_players():
    if request.method == 'POST':


        logged_in_user_id = User.query.filter_by(email=session['user']).first().id
        tournament_Name = request.form['tournament_name']

        db.session.add(Tournament(logged_in_user_id, tournament_Name))
        db.session.commit()
        session['tournament_Id'] = Tournament.query.filter_by(name=tournament_Name).first().id
        player_1_Name = request.form['player1']
        db.session.add(Player(player_1_Name,session['tournament_Id'],logged_in_user_id))
        player_2_Name = request.form['player2']
        db.session.add(Player(player_2_Name,session['tournament_Id'],logged_in_user_id))
        player_3_Name = request.form['player3']
        db.session.add(Player(player_3_Name,session['tournament_Id'],logged_in_user_id))
        player_4_Name = request.form['player4']
        db.session.add(Player(player_4_Name,session['tournament_Id'],logged_in_user_id))
        db.session.commit()

        player_1_Id = Player.query.filter_by(name = player_1_Name , owner_id = logged_in_user_id).first().id
        player_2_Id = Player.query.filter_by(name = player_2_Name , owner_id = logged_in_user_id).first().id
        player_3_Id = Player.query.filter_by(name = player_3_Name , owner_id = logged_in_user_id).first().id
        player_4_Id = Player.query.filter_by(name = player_4_Name , owner_id = logged_in_user_id).first().id


        session['player_1_Id'] = player_1_Id
        session['player_2_Id'] = player_2_Id
        session['player_3_Id'] = player_3_Id
        session['player_4_Id'] = player_4_Id
        return redirect('/score_input')

@app.route('/score_input', methods=['POST', 'GET'])
def score_input():
    this_Rounds_Players = []
    this_Rounds_Players += Player.query.filter_by(id = session['player_1_Id'])
    this_Rounds_Players += Player.query.filter_by(id = session['player_2_Id'])
    this_Rounds_Players += Player.query.filter_by(id = session['player_3_Id'])
    this_Rounds_Players += Player.query.filter_by(id = session['player_4_Id'])
    if 'hole_num' not in session:

        session['hole_num'] = 1
    if 'round_num' not in session: #This tracks the current round number being scored
        session['round_num'] = 1
        db.session.add(Round(session['round_num'],1)) #Instantiate a round with the given round number.
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=1)) #Connect each player to this new round
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=2))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=3))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=4))
        db.session.commit()
    #get the hole from the db for the par property
    hole = Hole.query.filter_by(id = session['hole_num']).first()
    return render_template('score_input.html', players=this_Rounds_Players, hole_num=session['hole_num'], round_num=session['round_num'],par_num=hole.par)

@app.route('/process_score', methods=['POST'])
def process_score():#Takes scores from the score_input template and puts them into the db.
    tournament_id = session['tournament_Id']

    #grab scores from form POST request
    player_1_Score = int(request.form['player_1_score'])
    player_2_Score = int(request.form['player_2_score'])
    player_3_Score = int(request.form['player_3_score'])
    player_4_Score = int(request.form['player_4_score'])

    #get the player ids using Session variable
    player_1_Id = Player.query.filter_by(name = session['player_1_Name']).first().id
    player_2_Id = Player.query.filter_by(name = session['player_2_Name']).first().id
    player_3_Id = Player.query.filter_by(name = session['player_3_Name']).first().id
    player_4_Id = Player.query.filter_by(name = session['player_4_Name']).first().id
    #create new score object using player ID, Round ID, Hole ID, Course ID, Tournament ID all from session and Score from the POST request
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=player_1_Id, tournament_id=session['tournament_Id'],score=player_1_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=player_2_Id, tournament_id=session['tournament_Id'],score=player_2_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=player_3_Id, tournament_id=session['tournament_Id'],score=player_3_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=player_4_Id, tournament_id=session['tournament_Id'],score=player_4_Score))


    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=session['player_1_Id'], tournament_id=session['tournament_Id'],score=player_1_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=session['player_2_Id'], tournament_id=session['tournament_Id'],score=player_2_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=session['player_3_Id'], tournament_id=session['tournament_Id'],score=player_3_Score))
    db.session.add(Score(round_id=session['round_num'], hole_id=session['hole_num'], course_id=session['course_id'], player_id=session['player_4_Id'], tournament_id=session['tournament_Id'],score=player_4_Score))
    session['hole_num'] += 1

    db.session.commit()

    #update the current hole number in the session variable
    session['hole_num'] += 1
    if session['hole_num'] > 18: #this logic will determine if all 18 holes have been played.
        session['hole_num'] = 1 #After 18 holes, hole is reset to 1
        session['round_num'] += 1 #Round is increased by 1
        db.session.add(Round(session['round_num'],tournament_id)) #New round is created in preparation for new scores
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=1)) #Player connected to new round
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=2))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=3))
        db.session.add(Round_Player_Table(round_id=session['round_num'],player_id=4))
        db.session.commit()
        return redirect('/leaderboard') #After last 18 holes, user sent to leaderboard
    return redirect('/score_input') #when there are more scores to report, user goes to next score_input template


@app.route('/list_tournaments')
def list_tournaments():#Used to display tournaments that a user can select to see their leaderboard
    if request.args.get('tournament_id'):
        tournament_id = request.args.get('tournament_id')

        some_Score = Score.query.filter_by(tournament_id = tournament_id).first()
        round_num = some_Score.round_id
        course_id = some_Score.course_id
        course = Course.query.filter_by(id = course_id).first().name
        player_scores = Score.query.filter_by(tournament_id = tournament_id).all()
        players = Player.query.filter_by(tournament_id = tournament_id).all()

        #get player id's for score query
        player_ids = {}
        j=1
        for player in players:
            player_ids['player_{0}_Id'.format(j)] = player.id
            j+=1
        #Set scores to zero
        player1total = 0
        player2total = 0
        player3total = 0
        player4total = 0
        #Query score database using player_ID and accumulate total scores
        player_1_Scores = Score.query.filter_by(player_id=player_ids['player_1_Id']).all()
        for score in player_1_Scores:
            player1total += score.score


        player_2_Scores = Score.query.filter_by(player_id=player_ids['player_2_Id']).all()
        for score in player_2_Scores:
            player2total += score.score


        player_3_Scores = Score.query.filter_by(player_id=player_ids['player_3_Id']).all()
        for score in player_3_Scores:
            player3total += score.score

        player_4_Scores = Score.query.filter_by(player_id=player_ids['player_4_Id']).all()
        for score in player_4_Scores:
            player4total += score.score

        all_Players_Total_Scores = player1total, player2total, player3total, player4total

        #get the player names for the template
        player_Names_Dict = {}
        i=0
        for player in players:
            player_Names_Dict['player_{0}_Name'.format(i)] = players[i].name
            i += 1
        #print(player_Names_Dict)

        last_hole_played = Score.query.order_by(desc(Score.hole_id)).first().hole_id

        return render_template("leaderboard.html", player_scores=all_Players_Total_Scores,round_num=round_num, player_Names_Dict=player_Names_Dict,course=course,last_hole_played=last_hole_played)
    else:
        tournaments = Tournament.query.all()
        if not tournaments:
            flash('There are currently no tournaments, sign-in and start one!')
            return redirect('/sign-in')
        return render_template('list_tournaments.html',tournaments=tournaments)


@app.route("/leaderboard", methods=['GET'])
def leaderboard():#populating score data assuming a for loop will be used in the template to list every players score'''
    if not Score.query.all():
        flash('Leaderboard is currently empty')
        return redirect('/')

    if request.method == 'GET':
        player1total = 0
        player2total = 0
        player3total = 0
        player4total = 0

        player_1_Scores = Score.query.filter_by(player_id=1)
        for score in player_1_Scores:
            player1total += score.score

        player_2_Scores = Score.query.filter_by(player_id=2)
        for score in player_2_Scores:
            player2total += score.score

        player_3_Scores = Score.query.filter_by(player_id=3)
        for score in player_3_Scores:
            player3total += score.score

        player_4_Scores = Score.query.filter_by(player_id=4)
        for score in player_4_Scores:
            player4total += score.score

        all_Players_Total_Scores = player1total, player2total, player3total, player4total


        player_1_Name = Player.query.filter_by(id = 1).first().name
        player_2_Name = Player.query.filter_by(id = 2).first().name
        player_3_Name = Player.query.filter_by(id = 3).first().name
        player_4_Name = Player.query.filter_by(id = 4).first().name
        player_names = [player_1_Name, player_2_Name,player_3_Name,player_4_Name]

        first_score = Score.query.first()
        round_id = first_score.round_id
        course_id = first_score.course_id
        round_num = Round.query.filter_by(id = round_id).first().round_number
        course = Course.query.filter_by(id = course_id).first().name
        last_hole_played = Score.query.order_by(desc(Score.hole_id)).first().hole_id
        #TODO find a better way to get last hole played

        return render_template("leaderboard.html", player_scores=all_Players_Total_Scores,round_num=round_num, player_names=player_names,course=course,last_hole_played=last_hole_played)


<<<<<<< HEAD
def logged_in_user():#creates a logged in user
    owner = User.query.filter_by(email=session['user']).first()
    return owner
=======
>>>>>>> list_tournanaments

endpoints_without_login = ['display_signup' , 'validate_user','list_tournaments', 'signin', 'static']

@app.before_request
def require_login():#Control for endpoint access for a non logged in user

    if not ('user' in session or request.endpoint in endpoints_without_login):
        return redirect("/signin")



# Our app secret key should be kept secret (i.e. not on github) upon app launch. (Not placed on github)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == '__main__':
    app.run()
