from re import A
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databaseShop.db"
# initialize the app with the extension
app.config['SIZE_COMMENT'] = 4
app.config['SIZE_PRODUCT'] = 10
app.secret_key = 'sdfsdfdsfsfcxvxcvsnvcvbvbcvfefdsf'
db = SQLAlchemy(app=app)
db.init_app(app)

login = LoginManager(app=app)