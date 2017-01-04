from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	if 'counter' in session:
		session['counter'] += 1 
	else:
		session['counter'] = 0
	return render_template('index.html')

@app.route('/reload', methods=['POST'])
def reload():
	session['counter'] += 2
	return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
		session['counter'] = 0
	return redirect('/')

app.run(debug=True)
