from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Course, Hole, Score 


@app.route("/")
def index():
   encoded_error = request.args.get("error")
   return render_template("signin.html", error=encoded_error and cgi.escape(encoded_error, quote=True))






if __name__ == '__main__':
    app.run()
