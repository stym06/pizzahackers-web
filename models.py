# Database models for PizzaHackers.
from main import db

class BaseModel(db.Model):
	"""
	Base model class for PizzaHackers.
	"""

	added = db.Column(db.DateTime)
	modified = db.Column(db.Datetime) 

class User(BaseModel):
	"""
	Member profile.
	"""

	id = db.column(db.Integer, primary_key=True)
	fb_id = db.column(db.String(40), unique=True)
	email = db.Column(db.String(40))

	name = db.column(db.String(120))
	batch = db.column(db.Integer)
	branch = db.column(db.String(10)) # TODO: Change to choices.
	registration_number = db.column(db.String(20))
	profile_image_url = db.column(db.string(120))
	
	twitter_id = db.column(db.String(40), unique=True)
	github_id = db.column(db.String(40), unique=True)

	proposals = db.relationship('Proposal', lazy='dynamic', backref='user')

class Proposal(BaseModel):
	"""
	Idea or hack proposal.
	A proposal can have upvotes, downvotes and comments.
	A user can vote only once on a proposal.
	"""

	id = db.Column(db.String(), primary_key=True)
	proposer = db.Column(db.Integer, db.ForeignKey('user.id'))
	title = db.Column(db.String(180))
	description = db.Column(db.Text)
	proposal_type = db.Column(db.String(10)) # Talk or hack. TODO: Change to choices.
	date = db.Column(db.DateTime)

	upvoters = db.Column(db.PickleType)
	downvoters = db.Column(db.PickleType)

	accepted = db.Column(db.Booolean)
	presented = db.Column(db.Boolean)

# class Hacks(BaseModel):
# 	"""
# 	Gallery for completed hacks / products.
# 	"""

# 	id = db.Column(db.Integer, primary_key=True)
# 	hackers = db.relationship('User', backref='hack', lazy='dynamic')
# 	title = db.Column(db.String(120))
# 	description = db.Column(db.Text)
# 	url = db.Column(db.String(120)) # TODO: Change to URLProperty.
# 	github = db.Column(db.String(120))