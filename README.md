# The golfscoreapp team presents


# Brief: 
This app will be used by Golfers and Golf Tournament directors to track and display player scores in real time which will increase tournament competition and transparency. 

# Stack: 
Python, Flask, Html, Css, Jinja2, JavaScript (adding in JS here - Katie)

# Git VCS: 
Utilizing a develp branch as described in this model- http://nvie.com/posts/a-successful-git-branching-model/

# Important golf score notes:
    1)A round of golf is played over 18 holes. After each hole, you should record your score on a scorecard (or in this case, our application) (May seem like common knowledge but its amazing how little I know about golf-Jonathan)
    2)Generally in golf, your opponent is responsible for keeping track of your score, and vise versa.


# User Stories:
User Story #1: The Scorekeeper
There will be one user that inputs scores for a group of 4 players. That user will first create a user account. Once created, they can sign in to the app and begin the score input process.

The score input process begins with setting up the group of players. The signed in user selects a course then types in the players' name. 

This will bring the user to a score input screen for Hole 1 where the user can begin inputing scores.

At the end of 18 holes of score inputs, the leaderboard screen displays the rounds end results.


User Story #2: Golf Player
A user not logged in should have access to a leaderboard screen that shows all scores for all players in that round. I envision a screen with a hyperlink list of courses (Only one in this iteration of the project), which opens to a screen of all the rounds played on that course (perhaps rounds are labeled by date/time of initial creation), that opens to a table showing each player, their total score, and differential from par based on how many holes they've played. That player is hyperlinked to a detailed page which shows their individual scores per hole.

# Design and Layout
Design will be created with HTML, CSS, and JavaScript. There will be 7 total screens. Links to the Wire Frames: https://ibb.co/gdjsWG, https://ibb.co/kjUjrG

    1) Sign-Up Page:  Page for the score keeper to sign up for an account.  Would request username, password, verify password and email address

    2) Sign-In Page: including a username field, a password field, a submit button and an optin to sign up for an account.

    3) List Courses Page - Will include a list of all the courses (comprised of 18 holes each).  Scorer can select the course they will be scoring.

    4) Tournament Initiation Page - Enables scorer to initiate a tournament and input the name of each player for the tournament.

    5) Score Input Page - Screen where scorer can input the number of swings for each player for each hole.  (there will actually be 18 of these, one for each hole)

    6) Leaderboard Page - Will list the players in the round and order them from the fewest number of swings to the most number of swings

    7) Independent Player Score - Will list the name of the player at the top of the screen and will then display the number of swings for each hole with the total listed at the bottom.



# STRETCH GOALS(not in priority order):
    1)Connect to some golfcourse API to integrate real golf course information such as names and par number for holes.
    2)Deploy Live?(Heroku)
    3)Reach goal will be to implement JavaScript that saves the data to the database immediately upon input instead of waiting for the user to hit a submit button.
    
# Test Plan:
How to get this working on your machine:

    1) Clone this repo to your machine.
    2) Activate a flask environment with these dependecies installed(using conda or another package manager alike): click 6.7 flask 0.12.2 flask-sqlalchemy 2.2 itsdangerous 0.24 jinja2 2.9.6 markupsafe 0.23 openssl 1.0.2l pip 9.0.1 pymysql 0.7.9 python 3.6.1 readline 6.2 setuptools 27.2.0 sqlalchemy 1.1.11 sqlite 3.13.0 tk 8.5.18 werkzeug 0.12.2 wheel 0.29.0 xz 5.2.2 zlib 1.2.8
    3) Create a mamp user with the name 'golfapp' and password 'golfapp' and check the 'Create database with same name and grant all privileges' box then click 'go'.
        a) Note: You can use whatever username and password that you would like but that you will need to modify the SQLALCHEMY_DATABASE_URI link to accomodate the new username and password.
    4) Within your favorite terminal, navigate to the project directory and enable your flask enviroment.
    5) Run 'python database_reset.py'. This will reset the database and add some hard coded data which is necessary for this prototype to run.
    6) Using MAMP, start Apache and MYSQL Servers.
    7) Start the local server with 'python main.py' from the terminal and go to the appropriate address that the server is ported to locally on your machine.
    8) From here create a new user by clicking on the 'Sign up' button.
    9) This will take you to a course selection page where you can pick any course and press 'Start Tournament' button.
    10) Type in the names of 4 players to start a round on the next screen.
    11) Now you can type the score for each of the players for each hole 1 through 18.
    12) After inputing scores for hole 18, the leaderboard will show total scores for round 1.
    Success!


This file was last modified by Dan
