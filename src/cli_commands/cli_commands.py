'''
CLI Commands for the app
'''


# Imports
from flask import Blueprint
from src import db


# Blueprint initialization
commands = Blueprint('commands', __name__)


# Flask CLI Commands
@commands.cli.command('create_db')
def db_create():
    """Creates the database using SQLAlchemy"""
    db.create_all()
    print('Database created!')


@commands.cli.command('drop_db')
def db_drop():
    """Drops the database using SQLAlchemy"""
    db.drop_all()
    print('Database dropped!')
