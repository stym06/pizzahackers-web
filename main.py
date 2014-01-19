from flask import Flask, request, render_template, redirect, session, \
	flash, g, abort, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.oauth import OAuth

from datetime import datetime

from config import *

# from models import BaseModel, User, Proposal

app = Flask(__name__)

app.config.update(
	DEBUG = DEBUG,
	SQLALCHEMY_DATABASE_URI = DB_URL,
	SECRET_KEY = SECRET
)

db = SQLAlchemy(app)
oauth = OAuth()

facebook = oauth.remote_app('facebook',
	base_url='https://graph.facebook.com/',
	request_token_url=None,
	access_token_url='/oauth/access_token',
	authorize_url='https://www.facebook.com/dialog/oauth',
	consumer_key=FACEBOOK_APP_ID,
	consumer_secret=FACEBOOK_APP_SECRET,
	request_token_params={'scope' : 'email,'})


class User(db.Model):
	"""
	Member profile.
	"""
	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	fb_id = db.Column(db.String(40), unique=True)
	email = db.Column(db.String(40))

	name = db.Column(db.String(120))
	batch = db.Column(db.Integer)
	branch = db.Column(db.String(10)) # TODO: Change to choices.
	registration_number = db.Column(db.String(20))
	profile_image_url = db.Column(db.String(120))
	
	twitter_id = db.Column(db.String(40), unique=True)
	github_id = db.Column(db.String(40), unique=True)

	proposals = db.relationship('Proposal', lazy='dynamic', backref='user')

	added = db.Column(db.DateTime)
	modified = db.Column(db.DateTime) 

class Proposal(db.Model):
	"""
	Idea or hack proposal.
	A proposal can have upvotes, downvotes and comments.
	A user can vote only once on a proposal.
	"""

	__tablename__ = 'Proposal'
	id = db.Column(db.String(), primary_key=True)
	proposer = db.Column(db.Integer, db.ForeignKey('User.id'))
	title = db.Column(db.String(180))
	description = db.Column(db.Text)
	proposal_type = db.Column(db.String(10)) # Talk or hack. TODO: Change to choices.
	date = db.Column(db.DateTime)

	upvoters = db.Column(db.PickleType)
	downvoters = db.Column(db.PickleType)

	accepted = db.Column(db.Boolean)
	presented = db.Column(db.Boolean)

	added = db.Column(db.DateTime)
	modified = db.Column(db.DateTime) 

@app.before_request
def check_user_status():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@app.route('/')
def home():
	""" Return index template at application root URL."""
	return render_template('home.html')

@app.route('/login')
def login():
	return facebook.authorize(callback=url_for('facebook_authorized',
		next=request.args.get('next') or request.referrer or None,
		_external=True))

@app.route('/logout')
def logout():
	sesison.clear()
	flash('You were logged out.')
	return redirect(url_for('home'))

@app.route('/login/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
	next_url = request.args.get('next') or url_for('home')
	if resp is None:
		flash('You denied the login.')
		return redirect(next_url)

	session['fb_access_token'] = (resp['access_token'], '')

	me = facebook.get('/me')

	user = User.query.filter_by(fb_id=me.data['id']).first()
	if user is None:
		user = User()
		user.fb_id = me.data['id']
		db.session.add(user)

	user.name = me.data['name']
	db.session.commit()
	session['user_id'] = user.id

	flash('You are now logged in as %s', user.name)
	return redirect(next_url)

@facebook.tokengetter
def get_facebook_auth_token():
	return session.get('fb_access_token')

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

if __name__ == '__main__':
	app.run()