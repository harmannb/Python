from flask import Flask, flash, render_template, redirect, request, session
import re
from mysqlconnection import MySQLConnector


emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
	if len(request.form['email']) < 1:
		flash('Email cannot be blank!')
	elif not emailRegex.match(request.form['email']):
		flash('Invaild Email Address!')
	else: 
		email = request.form['email']
    	session['email'] = email
        print mysql.query_db("SELECT * FROM users")
   	return redirect('/results')

@app.route('/results')
def show():
    print mysql.query_db("SELECT * FROM users")
    return render_template('results.html', email=session['email'])

app.run(debug=True)