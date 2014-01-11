# Database models for PizzaHackers.

from google.appengine.ext import ndb

class BaseModel(ndb.Model):
	"""
	Base model class for PizzaHackers.
	"""

	added = ndb.DateTimeProperty(auto_now_add = True)
	modified = ndb.DateTimeProperty(auto_now = True)

class User(ndb.BaseModel):
	"""
	Member profile.
	"""
	
	# TODO: Facebook Authentication.

	user_id = ndb.StringProperty(required=True) # Unique.
	fb_profile_url = ndb.StringProperty(required=True)
	access_token = ndb.StringProperty(required=True)

	name = ndb.StringProperty()
	batch = ndb.StringProperty()
	branch = ndb.StringProperty() # TODO: Change to choices.
	registration_number = ndb.StringProperty()
	profile_image_url = ndb.StringProperty()
	
	facebook_handle = ndb.StringProperty()
	twitter_handle = ndb.StringProperty()
	github_handle = ndb.StringProperty()

class Proposal(ndb.BaseModel):
	"""
	Idea or hack proposal.
	A proposal can have upvotes, downvotes and comments.
	A user can vote only once on a proposal.
	"""

	proposer = ndb.KeyProperty(kind = User)
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	proposal_type = ndb.StringProperty() # Talk or hack. TODO: Change to choices.
	slug = ndb.StringProperty()
	
	upvoters = ndb.ListProperty() # TODO: Fix this.
	downvoters = ndb.ListProperty()

	accepted = ndb.BoolProperty() # TODO: Fix this.

class Hacks(ndb.BaseModel):
	"""
	Gallery for completed hacks / products.
	"""

	hackers = ndb.ListProperty()
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	url = ndb.StringProperty() # TODO: Change to URLProperty.
	github = ndb.StringProperty()