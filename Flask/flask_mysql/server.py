from flask import Flask

from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsdb')
print('RIGHT ABOVE HERE')
print mysql.query_db("SELECT * FROM friends")

app.run(debug=True)