from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation, GenericForeignKey

import requests
import json

def has_changed(instance, field):
    if not instance.pk:
        return True
    old_value = instance.__class__._default_manager.\
             filter(pk=instance.pk).values(field).get()[field]
    return not getattr(instance, field) == old_value

class Hacker(models.Model):
	"""
	Profile of a user on PizzaHackers.
	"""

	BATCHES = (
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

	PLACEHOLDER_IMAGE_URL = "/static/core/img/placeholder_hacker.png"
	PLACEHOLDER_THUMBNAIL_URL = "/static/core/img/placeholder_hacker.png"

	# Basic information
	user = models.OneToOneField(User, related_name='hacker')
	batch = models.CharField(max_length=4, choices=BATCHES)
	branch = models.CharField(max_length=3, choices=BRANCHES)
	roll_number = models.CharField(max_length=12, unique=True)
	profile_image_url = models.CharField(max_length=255, default=PLACEHOLDER_IMAGE_URL)
	thumbnail_url = models.CharField(max_length=255, default=PLACEHOLDER_THUMBNAIL_URL)

	# Extra profile information
	bio = models.TextField(blank=True)
	interests = models.CharField(max_length=255, blank=True)
	blog = models.CharField(max_length=64, blank=True)
	github_id = models.CharField(max_length=32, blank=True)
	facebook_id = models.CharField(max_length=32, blank=True)
	twitter_id = models.CharField(max_length=32, blank=True)

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

	def full_name(self):
		return self.user.first_name + ' ' + self.user.last_name

	def _fetch_image_url(self, base_url):
		r = requests.get(base_url)
		if r.status_code == 200:
			data = json.loads(r.text)
			return data['data']['url']

	def _get_images(self):
		if self.facebook_id:
			self._profile_image_base = "http://graph.facebook.com/%s/picture?height=160&width=160&redirect=0" % self.facebook_id
			self._thumbnail_image_base = "http://graph.facebook.com/%s/picture?type=square&redirect=0" % self.facebook_id

			self._profile_image_url = self._fetch_image_url(self._profile_image_base)
			self._thumbnail_url = self._fetch_image_url(self._thumbnail_image_base)

			if self._profile_image_url and self._thumbnail_url:
				self.profile_image_url = self._profile_image_url
				self.thumbnail_url = self._thumbnail_url

	def save(self, *args, **kwargs):

		if has_changed(self, 'facebook_id'):
			self._get_images()
		super(Hacker, self).save(*args, **kwargs)

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
	slug = models.SlugField(blank=True, unique=True, max_length=150)
	type = models.CharField(max_length=4, choices=TYPES)
	tags = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	completed = models.BooleanField(default=False)
	url = models.CharField(max_length=128, blank=True)
	repo_url = models.CharField(max_length=128, blank=True)

	upvotes = models.ManyToManyField(Hacker, related_name='upvoters', blank=True)
	comments = GenericRelation('Comment')

	proposer = models.ForeignKey(Hacker, related_name='proposals')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Proposal, self).save(*args, **kwargs)
		self.slug = '%i-%s' % (self.id, slugify(self.title[:150]))
		super(Proposal, self).save(*args, **kwargs)

class Discussion(models.Model):
	"""
	A new topic of discussion.
	"""

	title = models.CharField(max_length=255, default='Untitled Discussion')
	tags = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	hacker = models.ForeignKey('Hacker', related_name='discussions')
	comments = GenericRelation('Comment')

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	"""
	Comments on discussions.
	"""

	comment = models.TextField(blank=True)
	user = models.ForeignKey(Hacker, related_name='comments')
	created = models.DateTimeField(auto_now_add=True)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	obj = GenericForeignKey('content_type', 'object_id')
	
	# discussion = models.ForeignKey('Discussion', related_name='comments',  blank=True, null=True)
	# proposal = models.ForeignKey('Proposal', related_name='comments',  blank=True, null=True)

	def __unicode__(self):
		return self.comment

	class Meta:
		ordering = ['-created']