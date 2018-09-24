from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myseckey'

class InfoForm(FlaskForm):

    username = StringField('Enter your User Name')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    username = ''
    form = InfoForm()
    if form.validate_on_submit():
        username = form.username.data
    return render_template('home.html', form=form, username = username)


if __name__ == '__main__':
    app.run(debug=True)
