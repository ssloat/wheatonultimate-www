import os

from flask import render_template
from app import app, forms

#from pymongo import MongoClient

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    groups = forms.GoogleGroupsSubscribe()
    return render_template('signup.html', title='Email lists', form=groups)

@app.route('/unsubscribe')
def unsubscribe():
    groups = forms.GoogleGroupsUnsubscribe()
    return render_template('unsubscribe.html', title='Email lists', form=groups)

@app.route('/kona')
def kona():
    return render_template('kona.html')

"""
@app.route('/verify')
def verify():
    groups = GoogleGroups()
    return render_template('verify.html', title='Email lists', form=groups)

@app.route('/ultimate')
def ultimate():
    threads = get_threads('wheaton-ultimate-frisbee')
    return render_template('topics.html', title='Ultimate', threads=threads)

@app.route('/housing')
def housing():
    threads = get_threads('wheaton-housing')
    return render_template('topics.html', title='Housing', threads=threads)

@app.route('/soccer')
def soccer():
    threads = get_threads('wheaton-soccer')
    return render_template('topics.html', title='Soccer', threads=threads)

@app.route('/social')
def social():
    threads = get_threads('wheaton-ultimate')
    return render_template('topics.html', title='Social', threads=threads)


@app.route('/google')
def google():
    return render_template('google.html')


def get_threads(group):
    mongo = MongoClient(os.environ.get('MONGO_DB_URI'))['slack']
    return mongo.threads.find({'group': group})
"""

