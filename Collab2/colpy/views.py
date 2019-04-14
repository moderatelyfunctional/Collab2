from django.shortcuts import render

# Create your views here.
def create(request):
	context = dict()

	return render(request, 'create.html', context)

def space(request, custom_url):
	context = dict()

	return render(request, 'space.html', context)