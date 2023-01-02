from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/vmuniversity.db'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from vmuniversity_flask import VMUniversity

