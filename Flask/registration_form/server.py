from flask import Flask, flash, render_template, redirect, request

import re

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def register():
	if len(request.form['email']) < 1:
		flash('Email cannot be blank!')
	elif not emailRegex.match(request.form['email']):
		flash('Invaild Email Address!')
	else:
		session['email'] = request.form['email']
	return redirect('/')

	if len(request.form['firstname']) < 1:
		flash('First Name: cannot be blank!')
	elif any (monkey.isdigits() for monkey in request.form['lastname'] 
		flash('Name cannot have numbers')
	return redirect('/', monkey=request.form)

	if len(request.form['lastname']) < 1:
		flash('Last Name: cannot be blank!')
	return redirect('/')
app.run(debug=True)