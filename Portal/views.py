from django.shortcuts import render
from django.http import Http404
from django.forms import modelformset_factory

import importlib

from . import models


from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.

def logout_view(request):
	"Log users out and re-direct them to the main page."
	logout(request)
	return HttpResponseRedirect('/')

def index(request):
	return render(request, 'index.html')