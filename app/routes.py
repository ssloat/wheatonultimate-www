from flask import render_template
from app import app

from app.forms import GoogleGroups

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    groups = GoogleGroups()
    return render_template('signup.html', title='Email lists', form=groups)

