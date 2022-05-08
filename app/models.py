from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
  #define schema(layout) for notes in our db
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.string(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
  #define schema(layout) for user in our db
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.string(100), unique=True)
  password = db.Column(db.string(100))
  first_name = db.Column(db.string(100))
  notes = db.relationship('Note')
