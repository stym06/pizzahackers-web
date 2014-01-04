import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py

from flask import Flask
from flask import render_template
app = Flask(__name__.split('.')[0])

@app.route('/')
def home():
	""" Return index template at application root URL."""
	return render_template('home.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/join')
def join():
	return render_template('join.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/rules')
def rules():
	return render_template('rules.html')

@app.route('/hacks')
def hacks():
	return render_template('hacks.html')