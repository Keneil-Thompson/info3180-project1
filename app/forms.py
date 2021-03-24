from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.core import DecimalField, IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = DecimalField('No. of Bathrooms', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    ptype = SelectField('Property Type', validators=[InputRequired()], choices=["House", "Apartment"])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    submit = SubmitField('Add property')
