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


'''@app.route("/tournament")
def create_tournament():'''

def logged_in_user():
    owner = User.query.filter_by(email=session['user']).first()
    return owner

endpoints_without_login = ['signup' ,'leaderboard', 'signin']

@app.before_request
def require_login():
    if not ('user' in session or request.endpoint in endpoints_without_login):
        print('wtf is going on')
        return redirect("/signin")



app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RU'

if __name__ == '__main__':
    app.run()
