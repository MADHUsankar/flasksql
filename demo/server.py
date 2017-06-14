from flask import Flask,render_template
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
# connect and store the connection in "mysql" note that you pass the database name to the function
 
@app.route('/') 
def display_usersone():
  users = mysql.query_db("SELECT * FROM users" ) 
  return render_template('firstpage.html',users=users)
# an example of running a query
 
@app.route('/<userid>') 
def display_userstwo(userid):
  query = "SELECT * FROM users WHERE idusers = :specific_id" 
  data = {'specific_id': userid}
  users = mysql.query_db(query,data) 
  return render_template('firstpage.html',one_user=users[0])

# an example of running a query
app.run(debug=True)