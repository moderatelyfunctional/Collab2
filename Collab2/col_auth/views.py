from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_in
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import CollabUser

# Create your views here.
def index(request):
	empty_context = dict()
	return render(request, 'index.html', empty_context)

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')

	default_context = dict()
	if request.method == 'GET':
		return render(request, 'login.html', default_context)
	
	email = request.POST.get('email')
	password = request.POST.get('password')
	user = CollabUser.objects.filter(email = email.lower())

	auth_user = authenticate(username = email.lower(), password = password)
	if not auth_user:
		default_context['email_field'] = email
		default_context['password_field'] = password
		if user.exists():
			default_context['error_text'] = 'The password is incorrect.'
		else:
			default_context['error_text'] = 'The email isn\'t associated with an account.'
		return render(request, 'login.html', default_context)

	auth_in(request, auth_user)
	return HttpResponseRedirect('/')

def signup(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/')

	default_context = dict()
	if request.method == 'GET':
		return render(request, 'signup.html', default_context)
	
	email = request.POST.get('email').lower()
	password = request.POST.get('password')
	confirmPassword = request.POST.get('password_conf')

	default_context['email_field'] = email
	default_context['password_field'] = password
	default_context['confirm_password'] = confirmPassword

	if password != confirmPassword:
		default_context['error_text'] = 'The password and the confirmation password don\'t match.'
		return render(request, 'signup.html', default_context)

	user = CollabUser.objects.create_user(email = email, password = password)

	auth_in(request, user)
	return HttpResponseRedirect('/')

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')	




