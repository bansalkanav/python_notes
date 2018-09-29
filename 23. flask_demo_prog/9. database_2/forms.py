from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo


class AddForm(FlaskForm):

    name = StringField('Name of User:', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    submit = SubmitField('Add User')

class DelForm(FlaskForm):

    id = IntegerField('Id of User to Remove:')
    submit = SubmitField('Remove User')
