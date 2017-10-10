from flask import request, redirect, render_template, session, flash
from app import app, db
from models import Course, Hole, Player, Round, Score, Tournament


@app.route("/")
def index():
    return "Hello!"





if __name__ == '__main__':
    app.run()
