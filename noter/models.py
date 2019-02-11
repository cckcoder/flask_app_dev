#! usr/bin/env python
from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from noter import db

class User(db.Model, UserMixin):

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(120), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password_hash = db.Column(db.String(80))
  notes = db.relationship('Note', backref='user', lazy='dynamic')

  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.set_password(password)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  @staticmethod
  def get_by_email(email):
    return User.query.filter_by(email=email).first()


class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(120))
  content = db.Column(db.Text)
  last_modified = db.Column(db.DateTime)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __init__(self, title, content, lastmodified, user_id):
    self.title = title
    self.content = content
    self.last_modified = lastmodified
    self.user_id = user_id

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
