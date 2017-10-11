from flask import request, redirect, render_template, session, flash
from app import app, db
from models import User, Tournament, Player, Round, Course, Hole, Score 


@app.route("/")
def index():
    return "Hello!"





if __name__ == '__main__':
    app.run()
