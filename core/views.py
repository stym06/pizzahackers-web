from django.shortcuts import render_to_response
from django.template import Context
from models import Hacker

# Create your views here.

def home(request):
	"""
	Render the homepage.
	"""
	c = Context({
			'title' : 'Home &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.',
			'user' : request.user
		})

	return render_to_response('home.html', c)

def login(request):
	"""
	Render the login page.
	"""

	c = Context({
			'title' : 'Login &raquo; Login to PizzaHackers.',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		})

	return render_to_response('login.html', c)

def join(request):
	"""
	Render the signup page.
	"""

	c = Context({
			'title' : 'Join &raquo; Join PizzaHackers and make a difference.',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.',
			'batches' : Hacker.BATCHES,
			'branches' : Hacker.BRANCHES
		})

	return render_to_response('join.html', c)

def rules(request):
	return render_to_response('rules.html')

def about(request):
	return render_to_response('about.html')

def hacks(request):
	return render_to_response('hacks.html')