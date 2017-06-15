from flask_bcrypt import Bcrypt
from flask import Flask, render_template, request, redirect,flash,session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="secret"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_REGEX = re.compile(r'^[a-zA-Z]+$')
mysql = MySQLConnector(app, 'registrations')
@app.route('/')
def index():
  return render_template("FORM.html")

@app.route('/result', methods=['POST'])
def create_user():
   print "Got Post Info"
   print request.form 

   firstname = request.form['firstname']
   lastname = request.form['lastname']
   emailid = request.form['emailid']
   password = request.form['password']
   pw_confirm = request.form['pw_confirm']

   print  name_REGEX.match(firstname) 
   print "regex displayed above"
   
   if len(firstname) < 3:
    flash("Please enter atleast two characters for First name")
   if (name_REGEX.match(firstname) == None):
    flash("Please enter only alpabets for First name")
   if len(lastname) < 3:
    flash("Please enter atleast two characters for Last name")
   if (name_REGEX.match(lastname) == None):
    flash("Please enter only alpabets for last name")
   if len(request.form['emailid']) < 1:
    flash("Email cannot be blank!")
   elif not EMAIL_REGEX.match(request.form['emailid']):
    flash("Invalid Email Address!")
   if len(password) <= 8:
    flash("Atleast 8 characters needed")
   elif password!=pw_confirm:
    flash("Password doesnot match")
   if(len(flash) < 1):
    return redirect('/')
   else:
     bcrypt.check_password_hash()
  
      query = "INSERT INTO regusers (first_name, last_name, emailid, password) VALUES (:first_name, :last_name, :emailid, :password)"
      data = {
              first_name: request.form['firstname'],
              last_name:request.form['lastname'],
              emailid:request.form['emailid'],
              password: request.form['password']
              }
      mysql.query_db(query, data)
      

   return render_template("result.html", name=firstname + " " + lastname)
app.run(debug=True) 