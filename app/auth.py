
from .models import User, Note
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

  #query the database for user info

    user = User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.home'))
      elif
        flash('Incorrect password, try again', category='error')
      else:
        flash('Email does not exist', category='error')
  return render_template("login.html", user = current_user)

#login view page
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for(auth.login))

#sign-up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get("email")
    first_name = request.form.get("first_name")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

#validating user info
  user = User.query.filter_by(email=email).first()
  if user:
   flash('Email already exists', category='error')
  elif len(email) < 4:
     flash("Email must be more that three charaters", category="error")
  elif len(first_name) < 5:
     flash("First Name must be more that five charaters", category="error")
  elif password1 != password2:
      flash("Passwords don\'t match", category="error")
  elif len(password1) < 7:
      flash("Email must be atleast seven charaters", category="error")
  else:
  #add user to database
   new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
   db.session.add(new_user)
   db.session.commit()
   login_user(new_user, remember=True)
   flash("Account created successfully!", category="success")  
   return redirect(url_for('views.home'))

  return render_template("sign_up.html", user=current_user)