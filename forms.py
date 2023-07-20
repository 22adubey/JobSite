from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class JobInput(FlaskForm):
    title = StringField('Job Title',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    submit = SubmitField('Submit')


