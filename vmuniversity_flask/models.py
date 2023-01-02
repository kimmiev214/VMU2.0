from vmuniversity_flask import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

user_course = db.Table('user_course',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

#this creates the user database object
class User(db.Model, UserMixin):
    '''Users database class'''
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    first_name=db.Column(db.String(20), nullable=True)
    last_name=db.Column(db.String(40), nullable=True)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    enrolledCourses = db.relationship('Course', secondary = user_course, backref='enrolledStudents')

    def __repr__(self):
        return f'{self.first_name} : {self.last_name} : {self.username} : {self.email} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}'

class Course(db.Model):
    '''Courses database class'''
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60), unique=False, nullable=False)
    description=db.Column(db.String(250), unique=False, nullable=True)
    professor=db.Column(db.String(30), unique=False, nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name} : {self.professor} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}'

#this creates the user database object
class Admin(db.Model, UserMixin):
    '''Users database class'''
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.email} : {self.date_created.strftime("%d/%m/%Y, %H:%M:%S")}'