from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True #displays runtime errors in the browser
#for use with local deployment
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://golfapp:golfapp@localhost:8889/golfapp'

#Connection string for heroku and using JAWSDB add-on.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wz4ok3xgjr71glb0:he72rvb5a6mzanm1@yhrz9vns005e0734.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/tof6y8gxby7h23os'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

import main