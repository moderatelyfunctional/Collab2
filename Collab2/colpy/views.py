from django.shortcuts import render
from django.http import HttpResponseRedirect

from col_auth.models import CollabUser, Space
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





