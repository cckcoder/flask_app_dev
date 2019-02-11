#! /usr/bin/env python
from flask import url_for, render_template
from flask_login import current_user, login_required
from . import app, lm
from .models import User, Note


@lm.user_loader
def load_user(user_id):
  return User.get(user_id)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/login')
def login():
  return render_template('login.html')

@login_required
@app.route('/home')
def home():
  return render_template('home.html')

@login_required
@app.route('/add')
def add():
  return render_template('new.html')

@login_required
@app.route('/view')
def view():
  return render_template('note.html')
