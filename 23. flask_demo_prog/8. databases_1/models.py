import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # This is a one-to-many relationship
    # A user can have many projects
    projects = db.relationship('Project',backref='user',lazy='dynamic')
    # This is a one-to-one relationship
    # A user only has one Supervisor, thus uselist is False.
    supervisor = db.relationship('Supervisor',backref='user',uselist=False)

    def __init__(self,name):
        self.name = name


    def __repr__(self):
        if self.supervisor:
            return "User name is {} and Supervisor is {}".format(self.name,self.supervisor.name)
        else:
            return "User name is {} and has no Supervisor assigned yet.".format(self.name)

    def report_projects(self):
        print("Here are my projects!")
        for project in self.projects:
            print(project.project_name)


class Project(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer,primary_key = True)
    project_name = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,project_name,user_id):
        self.project_name = project_name
        self.user_id = user_id


class Supervisor(db.Model):

    __tablename__ = 'supervisors'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use users.id because __tablename__='users'
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __init__(self,name,user_id):
        self.name = name
        self.user_id = user_id
