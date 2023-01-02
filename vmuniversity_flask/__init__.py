from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/vmuniversity.db'



db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'itncart@gmail.com'
app.config['MAIL_PASSWORD'] = 'temppasswordpython*123'

mail = Mail(app)

from vmuniversity_flask import VMUniversity

