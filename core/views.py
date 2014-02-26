from django.shortcuts import render_to_response
from django.template import Context

# Create your views here.

def home(request):
	"""
	Render the homepage.
	"""
	return render_to_response('home.html')

def login(request):
	return render_to_response('login.html')

def join(request):
	return render_to_response('join.html')

def rules(request):
	return render_to_response('rules.html')

def about(request):
	return render_to_response('about.html')

def hacks(request):
	return render_to_response('hacks.html')