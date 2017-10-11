from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Course, Hole, Score 


@app.route("/")
def index():
   encoded_error = request.args.get("error")
   return render_template("signin.html", error=encoded_error and cgi.escape(encoded_error, quote=True))

'''The following route pulls all the courses from the DB and puts them into
the courses variable which is sent to the template where a loop can pull 
the course name'''
@app.route("/courses")
def list_courses():
    courses = Course.query.all()
    return render_template("list-courses.html", courses=courses)




if __name__ == '__main__':
    app.run()
