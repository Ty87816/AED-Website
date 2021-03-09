from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, submitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20])
	
	email = StringField('Email', validators=[DataRequired(), Email()]
	
	password = PasswordField('Password', validators=[DataRequired()])
	
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	
	submit = submitField('Sign Up')
	
class RegistrationForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()]
	password = PasswordField('Password', validators=[DataRequired()])
	submit = submitField('Sign In)
	
	