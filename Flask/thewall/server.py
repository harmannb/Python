from flask import Flask, flash, render_template, redirect, request, session, flash
import re
from flask.ext.bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'walldb')
app.secret_key = "secret"
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    print session
    return render_template('index.html')

@app.route('/success')
def success():
    query = "SELECT * FROM users WHERE id=:id"
    values = {
        "id": session['user_id']
    }
    user = mysql.query_db(query, values)
    print user
    return render_template('the_wall.html', user=user[0])


@app.route('/register', methods=['POST'])
def register():
    valid = True
    if len(request.form['email']) < 1:
        flash('Please enter an email')
        valid = False
    if len(request.form['password']) < 1:
        flash('Please fill all fields')
        valid = False
    if valid: 
        query = "SELECT * FROM users WHERE email=:email"
        values = {
            "email": request.form['email']
        }
        user_info = mysql.query_db(query, values)
    if not user_info:
        flash('Please register')
        valid = False
    if user_info:
        if not bcrypt.check_password_hash(user_info[0]['password'], request.form['password']):
            flash('user does not match info in database')
            valid = False
    if not valid:
        return redirect('/')
    session['user_id'] = user_info[0]['id']
    return redirect ('/success')


@app.route('/create', methods=['GET','POST'])
def create():
    print request.form
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (:fname, :lname, :email, NOW())"
    values = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    mysql.query_db(query, values)
    return redirect('/')

app.run(debug=True)
