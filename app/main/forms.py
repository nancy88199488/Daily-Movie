from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class SubscribeForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    # category = SelectField('Category', choices=[('Action','Action'),('Comedy','Comedy'),('Drama','Drama')('Horror','Horror')],validators=[Required()])
    submit = SubmitField('Movie')

