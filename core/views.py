from django.shortcuts import render_to_response, render, redirect, \
			get_object_or_404				
from django.template import RequestContext
from django.contrib.auth.models import User
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required

from models import Hacker, Proposal

# Create your views here.

def home(request):
	"""
	Render the homepage.
	"""
	ctx = {
			'title' : 'Home &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	if not request.user.username:
		return render(request, 'home.html', ctx)

	else:
		ctx['title'] = 'Dashboard &raquo; PizzaHackers'
		ctx['hacker'] = request.user.hacker
		return render(request, 'dashboard.html', ctx)

def profile(request, username):
	"""
	Render the profile for a hacker.
	"""

	hacker = get_object_or_404(Hacker, user__username=username)

	full_name = ' '.join([hacker.user.first_name, hacker.user.last_name])

	ctx = {
			'title' : '%s &raquo; PizzaHackers' % full_name,
			'description' : hacker.bio,
			'hacker' : hacker,
			'full_name' : full_name
		}

	return render(request, 'profile.html', ctx)

@login_required
def account(request):
	"""
	Account page.
	"""

	user_fields = ['first_name', 'last_name', 'email']
	hacker_fields = ['bio', 'interests', 'facebook_id', 'twitter_id', 'github_id',
						'roll_number', 'batch', 'branch']

	hacker = request.user.hacker
	ctx = {
			'title' : 'Account &raquo; PizzaHackers',
			'description' : hacker.bio,
			'batches' : Hacker.BATCHES,
			'branches' : Hacker.BRANCHES
		}

	if request.method == 'POST':
		for field in user_fields:
			setattr(request.user, field, request.POST[field])
			request.user.save()
		for field in hacker_fields:
			setattr(request.user.hacker, field, request.POST[field])
			request.user.hacker.save()
		return redirect('/')

	return render(request, 'account.html', ctx)

def proposals(request, action=None, slug=None):
	"""
	Handle proposals.
	"""

	ctx = {
			'title' : 'Proposals &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	if request.method == 'POST':
		fields = ['title', 'type', 'description', 'tags', 'completed', 
				'url', 'repo_url']
		data = request.POST.dict()
		
		if data['completed'] == 'on':
			data['completed'] = True
		else:
			data['completed'] = False

		if data.has_key('slug'):
			proposal = get_or_404(Proposal, slug=data['slug'])
		else:
			proposal = Proposal(proposer=request.user.hacker)
		for field in fields:
			setattr(proposal, field, data[field])
			try:
				proposal.save()
			except Exception, e:
				ctx['error'] = e
				return render(request, 'proposals_edit.html', ctx)

		return redirect('/proposals')

	if action:
		ctx['types'] = Proposal.TYPES
		if action == 'new':
			ctx['title'] = 'Add a new proposal'
			return render(request, 'proposals_edit.html', ctx)

		else:
			slug = action
			proposal = get_object_or_404(Proposal, slug=slug)
			ctx['title'] = proposal.title
			ctx['proposal'] = proposal
			return render(request, 'proposal.html', ctx)



		# elif action == 'edit':
		# 	proposal = get_object_or_404(Proposal, slug=slug)
		# 	ctx['title'] = 'Edit &raquo; %s' % proposal.title
		# 	return render(request, 'proposals_edit.html', ctx)

	ctx['proposals'] = Proposal.objects.all()
	return render(request, 'proposals.html', ctx)

def login(request):
	"""
	Render the login page.
	"""

	ctx = {
			'title' : 'Login &raquo; Login to PizzaHackers.',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	if request.method == 'POST':
		data = request.POST.dict()

		user = auth.authenticate(username=data['username'],
								password=data['password'])
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return redirect('/')
			else:
				ctx['error'] = "This account has been disabled."
		else:
			ctx['error'] = "Invalid username / password."

	if request.user.username:
		return redirect('/')

	return render(request, 'login.html', ctx)

def join(request):
	"""
	Render the signup page.
	"""

	ctx = {
			'title' : 'Join &raquo; Join PizzaHackers and make a difference.',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.',
			'batches' : Hacker.BATCHES,
			'branches' : Hacker.BRANCHES
		}

	if request.method == 'POST':
		
		data = request.POST.dict()

		try:
			# Create a new User
			user = User.objects.create_user(username=data['username'], 
				email=data['email'], password=data['password'], 
				first_name=data['first_name'], last_name=data['last_name'])

			# Create a new Hacker
			hacker = Hacker.objects.create(user=user, batch=data['batch'],
						branch=data['branch'], roll_number=data['roll_number'],
						facebook_id=data['facebook_id'])

			ctx['success'] = "Registration successful! Please log in."

			authenticated_user = auth.authenticate(username=data['username'], 
												password=data['password'])

			auth.login(request, authenticated_user)

			return redirect('/')

		except Exception, e:
			# Render an error message
			ctx['error'] = e
			return render(request, 'join.html', ctx)

	else:

		if request.user.username:
			return redirect('/')

		return render(request, 'join.html', ctx)

def rules(request):
	ctx = {
			'title' : 'Rules &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	return render(request, 'rules.html', ctx)

def hackers(request):
	hackers = Hacker.objects.all()
	ctx = {
			'title' : 'Hackers &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.',
			'hackers' : hackers
		}
	return render(request, 'hackers.html', ctx)

def about(request):
	ctx = {
			'title' : 'About &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	return render(request, 'about.html', ctx)

def hacks(request):
	return render_to_response('hacks.html')