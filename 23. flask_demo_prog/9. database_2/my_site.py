import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64), unique=True)
    name = db.Column(db.Text)

    def __init__(self,name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "User name: {} and Email: {}".format(self.name, self.email)

############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        # Add new User to database
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('list_user'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_user():
    # Grab a list of Users from database.
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/delete', methods=['GET', 'POST'])
def del_user():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('list_user'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
