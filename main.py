from flask import request, redirect, render_template
from app import app, db
from models import Course, Hole, Player, Round
