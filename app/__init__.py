from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc'
app.config['WTF_CSRF_ENABLED'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql:///todolist"

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

