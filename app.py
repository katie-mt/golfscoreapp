from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True #displays runtime errors in the browser
app.config['SQLALCHEMY_DATABASE_URI'] = #SQL URI goes here after I create
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
