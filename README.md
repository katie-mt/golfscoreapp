# golfscoreapp
Golf Score App
This app is going to be designed to allow players to easily keep track of their score throughout gameplay.

Stack: Python, Flask, Html, Css, Jinja2, JavaScript (adding in JS here - Katie)
Git VCS: Utilizing a develp branch as described in this model- http://nvie.com/posts/a-successful-git-branching-model/

Important golf score notes:
    1)A round of golf is played over 18 holes. After each hole, you should record your score on a scorecard (or in this case, our application) (May seem like common knowledge but its amazing how little I know about golf-Jonathan)
    2)Generally in golf, your opponent is responsible for keeping track of your score, and vise versa.

Some thoughts I've(Dan) been writing down and want to share:
1. I can see potentially 6 objects or models: Course, Hole, Round, Score, Player.

Course- Has many Holes associated to one course. No ability to create more courses, future feature buildout possible.

Hole- Has many rounds and has many players. Hole has par field. No ability to create more holes, future feature buildout possible.

Round- Has one course, has many Players and Holes. Full CRUD Ability.

Score- Has one player, one round, one Hole. This stores the stroke count for each unique player on each unique hole and each unique round. Full CRUD.

Player- Would be nice feature to CRUD players and keep stats however initial build could be no ability to create new players and will need players preprogrammed as "Player 1", "Player 2". Create a round using the "Player 1", "Player 2" names.

Additionally, I think we should have one User object that can log in as a Score Reporter.

User Stories:

User Story #1:  The Scorekeeper
We can assume there will be one person logging in to report scores in real time after each hole. This can be one user. (Think of a group of 4 golfers come to the end of their hole, they call/text the tournament director to report scores. That tournament direct actually inputs scores to update real time progress.)  This scorekeeper will use the app to keep score for each of the golf players

User Story #2:  Golf Player
A user not logged in should have access to a leaderboard screen that shows all scores for all players in that round. I envision a screen with a hyperlink list of courses (Only one in this iteration of the project), which opens to a screen of all the rounds played on that course (perhaps rounds are labeled by date/time of initial creation), that opens to a table showing each player, their total score, and differential from par based on how many holes they've played. That player is hyperlinked to a detailed page which shows their individual scores per hole.

Design and Layout

There will be 6 total screens:

(1) Sign-Up Page:  Page for the score keeper to sign up for an account.  Would request username, password, verify password and email address

(2) Sign-In Page: including a username field, a password field, a submit button and an optin to sign up for an account.

(3) List Courses Page - Will include a list of all the courses (comprised of 18 holes each).  Scorer can select the course they will be scoring.

(4) Tournament Initiation Page - Enables scorer to initiate a tournament and input the name of each player for the tournament.

(5) Score Input Page - Screen where scorer can input the number of swings for each player for each hole.  (there will actually be 18 of these, one for each hole)

(6) Leaderboard Page - Will list the players in the round and order them from the fewest number of swings to the most number of swings

(7) Independent Player Score - Will list the name of the player at the top of the screen and will then display the number of swings for each hole with the total listed at the bottom.


Design will be created with HTML, CSS, and JavaScript

Reach goal will be to implement JavaScript that saves the data to the database immediately upon input instead of waiting for the user to hit a submit button.

STRETCH GOALS(not in any specific order):
1)Connect to some golfcourse API to integrate real golf course information such as names and par number for holes.
2)Deploy Live?(Heroku)

Links to the Wire Frames -
https://ibb.co/gdjsWG
https://ibb.co/kjUjrG

How to get this working on your machine:
1) clone this repo to your machine.
2) activate a flask environment with these dependecies installed(using conda or another package manager alike):
click 6.7
flask 0.12.2
flask-sqlalchemy 2.2
itsdangerous 0.24
jinja2 2.9.6
markupsafe 0.23
openssl 1.0.2l
pip 9.0.1
pymysql 0.7.9
python 3.6.1
readline 6.2
setuptools 27.2.0
sqlalchemy 1.1.11
sqlite 3.13.0
tk 8.5.18
werkzeug 0.12.2
wheel 0.29.0
xz 5.2.2
zlib 1.2.8
3) Create a mamp user with the name 'golfapp' and password 'golfapp'(note that you CAN use whatever username and password that you would like but that you will need to modify the SQLALCHEMY_DATABASE_URI link to accomodate the new username and password.) and check the 'Create database with same name and grant all privileges' box then click 'go'.
4) Next from the command line run '$ python database_reset.py' while in the project directory(note '$' represents a terminal  command do not actually include in the command). This will reset the database and add some hard coded data in there necessary for the minimum viable product to run. 
5) Then start the local server with '$ python main.py' from the terminal and go to the appropriate address that the server is ported to locally on your machine. 
6) From here you can then create a new user and start keeping track of your golf scores!

This file was last modified by jjames1011

