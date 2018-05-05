from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, DecimalField, TextAreaField, validators, StringField, SubmitField
from interest import getInfo
import os

ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default=False)
if ENVIRONMENT_DEBUG.lower() in ("f", "false"):
    ENVIRONMENT_DEBUG=False

DEBUG = ENVIRONMENT_DEBUG

SECRET_KEY = os.environ.get("SECRET_KEY", default=None)

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
if not SECRET_KEY:
    raise ValueError("No secret key set for flask application")


class InterestForm(Form):
	principle = DecimalField('Principle: ', validators = [validators.required()])
	rate = DecimalField('Interest rate: ', validators = [validators.required()])
	monthly = DecimalField('Monthly Contributions (leave blank for none): ')
	compound = DecimalField('Compounding frequency (leave blank for monthly): ')
	time = DecimalField('Time (in years): ', validators = [validators.required()])

@app.route('/', methods=['GET', 'POST'])
def interest():
	form = InterestForm(request.form)
	final = ''
	print(form.errors)
	if request.method == 'POST':
		principle = request.form['principle']
		rate = request.form['rate']
		monthly = request.form['monthly']
		compound = request.form['compound']
		time = request.form['time']

		if not compound:
			compound = 12


		if form.validate():
			final = getInfo(principle, rate, time, monthly, compound)
		else:
			flash('Principle, rate, and time fields are required')

	return render_template('interest.html', form = form, interest = final)
