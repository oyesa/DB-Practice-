from crypt import methods
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  data = request.form
  print(data)
  return render_template("login.html")

@auth.route('/logout')
def logout():
  return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get("email")
    firstName = request.form.get("firstName")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

#validating user info
  if len(email)<4:
     pass
  elif len(firstName)<4:
     pass
  elif password1 != passwaord2:
      pass
  elif len(password1) < 7:
      pass
  else:
  #add user to database

  
   return render_template("sign_up.html")