from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty")
		return redirect('/')
	return render_template('results.html', monkey=request.form)


app.run(debug=True)