from flask import Flask, render_template, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'secret'

def setSession():
	session['counter'] = random.randint(1,100)

@app.route('/')
def index():
	if session['counter'] == None:
		setSession()
	print session['counter']
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	guess = request.form['guess']
	if request.method == 'POST':
		if guess.isdigit():
			numguess = int(guess)
			if numguess > session['counter']:
				print "Too High"
	else:
		print "Too Low"
	return redirect('guess.html', monkey=request.form)

@app.route('/reset', methods=['GET','POST'])
def reset():
	setSession()
	return redirect('/')

app.run(debug=True)


