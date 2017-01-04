from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret'

newgold = 0

@app.route('/')
def index():
	session['total'] = 0
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	hiddeninput = request.form['hidden']

	if hiddeninput == 'farm':
		newgold = random.randint(10,20)

	elif hiddeninput == 'cave':
		newgold = random.randint(5,10)
	
	elif hiddeninput == 'house':
		newgold = random.randint(2,5)

	elif hiddeninput == 'casino':
		newgold = random.randint(-50,50)

	session['total'] += newgold

	return render_template('index.html', total=session['total'])
app.run(debug=True)