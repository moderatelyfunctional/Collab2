from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
	empty_context = dict()
	return render(request, 'index.html', empty_context)