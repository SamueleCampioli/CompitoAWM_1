from django.shortcuts import render
from django.http import Http404
from django.forms import modelformset_factory

import importlib

from . import models
from . import forms


from django.http import HttpResponseRedirect
from django.contrib.auth import logout


#######################################################################################################################
# Form-based interface: server-side only
#######################################################################################################################

def node_form(request):
	# NodeFormset=modelformset_factory(models.Node, form=forms.NodeForm)
	NodeFormset = modelformset_factory(models.Node, form=forms.NodeForm, can_delete=True)
	if request.method == 'POST':
		formset = NodeFormset(request.POST)
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.user = request.user
				instance.save()
	else:
		formset = NodeFormset(queryset = models.Node.objects.filter(user = request.user))
	return render(request, 'nodes.html', {'formset': formset, "capabilities": models.capabilities})


def capability_form(request, node_id, capability):
    # get model class
    if capability in models.capabilities:
        cap = models.capabilities[capability]
        # print(cap["name"])
        model = getattr(importlib.import_module("RaspNodeConfig.models"), cap["model"])
        form = getattr(importlib.import_module("RaspNodeConfig.forms"), cap["form"])
    else:
        raise Http404('Capability not found')
    CapabilityFormset = modelformset_factory(model, form=form, can_delete=True)
    if request.method == 'POST':
        formset = CapabilityFormset(request.POST, queryset=model.objects.filter(node__exact=node_id))
        if formset.is_valid():
            formset.save()
    else:
        # formset = CapabilityFormset(queryset=model.objects.filter(node__id__exact=node_id))
        formset = CapabilityFormset(queryset=model.objects.filter(node__exact=node_id))
    return render(request, 'capabilities.html', {'formset': formset})

def logout_view(request):
	"Log users out and re-direct them to the main page."
	logout(request)
	return HttpResponseRedirect('/')

def index(request):
	return render(request, 'index2.html')