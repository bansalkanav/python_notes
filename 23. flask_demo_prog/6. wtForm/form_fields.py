from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'myseckey'

class InfoForm(FlaskForm):
    username = StringField('Enter your name',validators=[DataRequired()])
    grad  = BooleanField("Have you completed your Graduation?")
    degree = RadioField('Please choose your degree:', choices=[('btech','Bachelors of Tech'),('bcom','Bachelores of Com')])
    language = SelectField('Select any one:',
                          choices=[('eng', 'English'), ('pun', 'Punjabi'),
                                   ('hindi', 'Hindi')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():

        session['username'] = form.username.data
        session['grad'] = form.grad.data
        session['degree'] = form.degree.data
        session['language'] = form.language.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))


    return render_template('home.html', form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
