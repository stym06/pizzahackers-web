import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py

from flask import Flask, render_template, redirect, session
# from flask_oauth import OAuth

from config import *

app = Flask(__name__.split('.')[0])
app.debug = DEBUG
app.secret_key = SECRET
# oauth = OAuth()

# Set up Facebook Auth
# facebook = oauth.remote_app('facebook',
# 	base_url='https://graph.facebook.com/',
# 	request_token_url=None,
# 	access_token_url='/oauth/access_token',
# 	authorize_url='https://www.facebook.com/dialog/oauth',
# 	consumer_key=FACEBOOK_APP_ID,
# 	consumer_secret=FACEBOOK_APP_SECRET,
# 	request_token_params={'scope' : 'email,'})

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