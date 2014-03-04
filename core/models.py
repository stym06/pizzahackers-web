from django.db import models
from django.contrib.auth.models import User

class Hacker(models.Model):
	"""
	Profile of a user on PizzaHackers.
	"""

	YEARS = (
		('2010', '2010'),
		('2011', '2011'),
		('2012', '2012'),
		('2013', '2013')
	)

	BRANCHES = (
		('CSE', 'Computer Science and Engg.'),
		('ECE', 'Electronics and Communication Engg.'),
		('EEE', 'Electrical and Electronics Engg.'),
		('ME', 'Mechanical Engg.'),
		('PIE', 'Production and Industrial Engg.'),
		('MME', 'Metallurgy and Materials Engg')
	)

	# Basic information
	user = models.OneToOneField(User, related_name='user')
	batch = models.CharField(max_length=4, choices=YEARS)
	branch = models.CharField(max_length=3, choices=BRANCHES)
	roll_number = models.CharField(max_length=12)

	# Extra profile information
	bio = models.TextField(blank=True)
	blog = models.CharField(max_length=64, blank=True)
	github_id = models.CharField(max_length=32, blank=True)
	facebook_id = models.CharField(max_length=32, blank=True)
	twitter_id = models.CharField(max_length=32, blank=True)

class Proposal(models.Model):
	"""
	A proposal for idea / hack / talk.
	"""

	# TODO: Add voting.

	TYPES = (
		('HACK', 'Hack'),
		('TALK', 'Talk'),
	)

	title = models.CharField(max_length=255)
	slug = models.SlugField(blank=True, unique=True)
	type = models.CharField(max_length=4, choices=TYPES)
	description = models.TextField()
	proposer = models.OneToOneField(Hacker, related_name='proposer')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)