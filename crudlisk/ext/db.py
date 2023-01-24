from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import create_models

import sqlite3


def create_db(app):
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # tables
    #user = User

    create_models(db)

   # class User(db.Model):
   #     __tablename__ = "Users"
   #     id = db.Column(db.Integer, primary_key=True)
   #     username = db.Column(db.String(30), unique=True, nullable=False)
   #     email = db.Column(db.String)
   #     age = db.Column(db.Integer, nullable=False)

    return db

