from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    ptype = SelectField('Property Type', choices=[(-1, '--Select Property Type--'),(1, 'House'), (2, 'Apartment')], validators=[DataRequired()], coerce=int)
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
