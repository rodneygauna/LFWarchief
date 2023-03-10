'''
User forms for the application.
'''


# Imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from src.models import User


# Register user form
class RegisterUserForm(FlaskForm):
    '''Register user form'''

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'pass_confirm', message='Passwords must match.')])
    pass_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        '''Check if email is already registered.'''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already registered.')

    def check_username(self, field):
        '''Check if username is already in use.'''
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already in use.')


# Form - Edit User Profile
class EditUserForm(FlaskForm):
    '''Form to edit a user profile'''

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save')

    def check_email(self, field):
        '''Check if email is already registered.'''
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already registered.')

    def check_username(self, field):
        '''Check if username is already in use.'''
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already in use.')


# Form - Login
class LoginForm(FlaskForm):
    '''Form to login a user'''

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
