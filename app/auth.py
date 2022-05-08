from crypt import methods
from flask import Blueprint, render_template, request, flash

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
  if len(email) < 4:
     flash("Email must be more that three charaters", category="error")
  elif len(firstName) < 5:
     flash("First Name must be more that five charaters", category="error")
  elif password1 != password2:
      flash("Passwords don\'t match", category="error")
  elif len(password1) < 7:
      flash("Email must be atleast seven charaters", category="error")
  else:
  #add user to database
   flash("Account created successfully!", category="success")

   return render_template("sign_up.html")