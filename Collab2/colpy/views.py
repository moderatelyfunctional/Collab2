import os
import random
import subprocess

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from col_auth.models import CollabUser, Space
from .data import create_space_url

# Create your views here.
def create(request):
	context = dict()
	collab_user = CollabUser.objects.get(email = request.user.email)
	collab_user_spaces = collab_user.spaces.all()

	context['new_space_url'] = 'Papaya,Umber,Jaxon'
	# while True:
	# 	new_space_url = create_space_url()
	# 	if not collab_user_spaces.filter(url = create_space_url).exists():
	# 		Space.objects.create(url = new_space_url, host = collab_user)
	# 		context['new_space_url'] = new_space_url
	# 		break

	return render(request, 'create.html', context)

def space(request, custom_url):
	context = dict()
	context['space_url'] = custom_url

	if not request.user.is_authenticated:
		context['user_type'] = 'participant'
		return render(request, 'space.html', context)

	if not Space.objects.filter(url = custom_url).exists():
		return render(request, 'no_space.html', context)

	collab_user = CollabUser.objects.get(email = request.user.email)
	space = Space.objects.get(url = custom_url)

	if space.host == collab_user:
		context['user_type'] = 'host'
	else:
		context['user_type'] = 'participant'

	return render(request, 'space.html', context)

def delete_space(request):
	space_url = request.POST.get('space_url')

	collab_user = CollabUser.objects.get(email = request.user.email)
	space = Space.objects.filter(url = space_url).first()

	if space.host == collab_user:
		space.delete()
	
	return HttpResponseRedirect('/')

@csrf_exempt
def run_python(request):
	code = request.POST.get('python_code')
	code_filename = 'run_python/{}.py'.format(random.random())
	with open(code_filename, 'w') as python_out:
		for line in code:
			python_out.write(line)

	p = subprocess.Popen(['python', code_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	os.remove(code_filename)
	
	if err:
		response = err
	else:
		response = out
	return HttpResponse(response)








