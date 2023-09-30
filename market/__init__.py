from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3708e13c55d735b237a8f81a'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes