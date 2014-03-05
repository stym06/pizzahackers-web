from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
import django.contrib.auth as auth

from models import Hacker

# Create your views here.

def home(request):
	"""
	Render the homepage.
	"""
	ctx = {
			'title' : 'Home &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	return render(request, 'home.html', ctx)

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
						branch=data['branch'], roll_number=data['roll_number'])

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
		return render(request, 'join.html', ctx)

def rules(request):
	ctx = {
			'title' : 'Rules &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	return render(request, 'rules.html', ctx)

def about(request):
	ctx = {
			'title' : 'About &raquo; PizzaHackers - Doers of NIT Jamshedpur',
			'description' : 'PizzaHackers is the doer community of NIT Jamshedpur.'
		}

	return render(request, 'about.html', ctx)

def hacks(request):
	return render_to_response('hacks.html')