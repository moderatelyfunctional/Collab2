import os
import json
import random
import subprocess

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from col_auth.models import CollabUser, Space, Submission
from .data import create_space_url

# Create your views here.
def create(request):
	context = dict()
	collab_user = CollabUser.objects.get(email = request.user.email)
	collab_user_spaces = collab_user.spaces.all()

	while True:
		new_space_url = create_space_url()
		if not collab_user_spaces.filter(url = create_space_url).exists():
			Space.objects.create(url = new_space_url, host = collab_user)
			context['new_space_url'] = new_space_url
			break

	return render(request, 'create.html', context)

def space(request, custom_url):
	context = dict()
	context['space_url'] = custom_url

	if Space.objects.filter(url = custom_url).count() == 0:
		return render(request, 'no_space.html', context)

	space = Space.objects.get(url = custom_url)
	context['space_code'] = space.code

	if not request.user.is_authenticated:
		context['user_type'] = 'participant'
		return render(request, 'space_participant.html', context)

	collab_user = CollabUser.objects.get(email = request.user.email)
	if space.host == collab_user:
		context['user_type'] = 'host'
		return render(request, 'space_admin.html', context)
	else:
		context['user_type'] = 'participant'
		return render(request, 'space_participant.html', context)

def gotospace(request):
	context = dict()
	custom_url = request.POST.get('custom_url')
	return HttpResponseRedirect('/space/' + custom_url)

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

@csrf_exempt
def pull_python(request):
	space_url = request.POST.get('space_url')
	space = Space.objects.filter(url = space_url).first()

	data = {'python_code': space.code}
	return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def update_python(request):
	space_url = request.POST.get('space_url')
	python_code = request.POST.get('python_code')

	collab_user = CollabUser.objects.get(email = request.user.email)
	space = Space.objects.filter(url = space_url).first()

	if space.host != collab_user:
		return HttpResponseBadRequest('Sorry you are not the host of the space')

	space.code = python_code
	space.save()
	return HttpResponse('The code was updated!')

@csrf_exempt
def submit_python(request):
	space_url = request.POST.get('space_url')
	python_code = request.POST.get('python_code')

	space = Space.objects.filter(url = space_url).first()
	curr_submission = Submission.objects.create(submission_code = python_code)
	space.submission.add(curr_submission)
	space.save()

	return HttpResponse('Thanks for submitting!')

@csrf_exempt
def fetch_submission(request):
	space_url = request.POST.get('space_url')
	collab_user = CollabUser.objects.get(email = request.user.email)
	space = Space.objects.filter(url = space_url).first()

	submissions = space.submission.all()
	random_submission = submissions[int(len(submissions) * random.random())]
	code = random_submission.submission_code

	space.submission.clear()
	for submission in submissions:
		submission.delete()
	space.save()

	data = {'python_code': code}
	return HttpResponse(json.dumps(data), content_type='application/json')
