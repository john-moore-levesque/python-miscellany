from flask import Flask, render_template, flash, request
from wtforms import Form, IntegerField, SelectField, validators
from collatz import collatz
from fibonacci import fib
from pollardrho import rho
from pi import leibniz, bbp
import os


ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default=False)
if str(ENVIRONMENT_DEBUG).lower() in ("f", "false"):
    ENVIRONMENT_DEBUG = False

DEBUG = ENVIRONMENT_DEBUG

SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
if not SECRET_KEY:
    raise ValueError("No secret key set for flask application")


class UserInput(Form):
    number = IntegerField('Number: ', validators=[validators.required()])


class PRhoInput(Form):
    start = IntegerField('Start: ', validators=[validators.required()])
    numToFactor = IntegerField('Number To Factor: ', validators=[validators.required()])


class ChoiceForm(Form):
    choiceform = SelectField("Choice",
                    choices=[('Pi', 'pi.html'),
                            ('Pollard\'s Rho', 'pollardrho.html'),
                            ('Collatz', 'collatz.html'),
                            ('Fibonacci', 'fibonacci.html')])


@app.route('/', methods=['GET', 'POST'])
def dropdown():
    # To-Do:
    # Implemet dropdown menu on root page to take you to the different
    #  math function pages
    form = ChoiceForm(request.form)
    choice = ""
    if request.method == 'POST':
        choice = request.form['mathfunctions']
    return render_template('math.html', form=form, choice=choice)


@app.route('/collatz', methods=['GET', 'POST'])
def collatzpage():
    form = UserInput(request.form)
    print(form.errors)
    clist = []
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
        except ValueError:
            number = 2

        if form.validate():
            clist = list(collatz(number))

    return render_template('collatz.html', form=form, clist=clist)


@app.route('/fibonacci', methods=['GET', 'POST'])
def fibpage():
    form = UserInput(request.form)
    print(form.errors)
    flist = []
    if request.method == 'POST':
        number = request.form['number']
        try:
            number = int(number)
        except ValueError:
            number = 2

        if form.validate():
            flist = list(fib(number))
        else:
            flist = "Please provide an integer greater than or equal to 2"

    return render_template('fibonacci.html', form=form, flist=flist)


@app.route('/pollardrho', methods=['GET', 'POST'])
def rhopage():
    form = PRhoInput(request.form)
    print(form.errors)
    factors = None
    if request.method == 'POST':
        start = request.form['start']
        numToFactor = request.form['numToFactor']
        try:
            start = int(start)
        except ValueError:
            start = 2
        print(start)

        try:
            numToFactor = int(numToFactor)
        except ValueError:
            numToFactor = 2
        print(numToFactor)

        if form.validate():
            factors = rho(start, numToFactor)
        else:
            print(form.validate())

        print(factors)

    return render_template('pollard-rho.html', form=form, factors=factors)


@app.route('/pi', methods=['GET', 'POST'])
def pipage():
    form = UserInput(request.form)
    print(form.errors)
    lpi = 0
    bbppi = 0
    if request.method == 'POST':
        number = request.form['number']

        try:
            number = int(number)
        except ValueError:
            number = 0

        if form.validate():
            lpi = leibniz(number)
            bbppi = bbp(number)

    return render_template('pi.html', form=form, leibniz=lpi, bbp=bbppi)

if __name__ == '__main__':
    app.run()
