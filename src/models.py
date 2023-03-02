'''
This file contains the models for the database.
'''


# Imports
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from src import db, login_manager


# Model - Users
@login_manager.user_loader
def load_user(user_id):
    '''Returns the user object based on the user id'''
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    '''User account model'''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(
        db.String(255), nullable=False, default='default_profile.jpg')
    email = db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''Checks if the password is correct'''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username}"
