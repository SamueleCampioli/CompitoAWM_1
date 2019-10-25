from django.shortcuts import render, redirect
from django.http import Http404
from django.forms import modelformset_factory

import importlib

from . import models
from . import forms


from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#######################################################################################################################
# Form-based interface: server-side only
#######################################################################################################################
#@login_required()
def room_form(request):
	RoomFormset = modelformset_factory(models.Room, form=forms.RoomForm, can_delete=True)
	if request.method == 'POST':
		formset = RoomFormset(request.POST)
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.user = request.user
				instance.save()
			for instance in formset.deleted_objects:
				instance.delete()
			return redirect('room_form')
	else:
		if request.user.is_authenticated:
			formset = RoomFormset(queryset = models.Room.objects.filter(user = request.user))
		else:
			formset = RoomFormset()
	return render(request, 'room.html', {'formset': formset})

#@login_required
def node_form(request, room_id):
	# NodeFormset=modelformset_factory(models.Node, form=forms.NodeForm)
	NodeFormset = modelformset_factory(models.Node, form=forms.NodeForm, can_delete=True)
	if request.method == 'POST':
		formset = NodeFormset(request.POST)
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.user = request.user
				instance.room = models.Room.objects.filter(id__exact = room_id).get()
				instance.save()
			for instance in formset.deleted_objects:
				instance.delete()
			return redirect('node_form', room_id = room_id)
	else:
		if request.user.is_authenticated:
			formset = NodeFormset(queryset = models.Node.objects.filter(user__exact = request.user, room__exact = room_id))
		else:
			formset = NodeFormset()
	return render(request, 'nodes.html', {'formset': formset, "capabilities": models.capabilities})

#@login_required
def capability_form(request, room_id, node_id, capability):
	# get model class
	if capability in models.capabilities:
		cap = models.capabilities[capability]
		model = getattr(importlib.import_module("RaspNodeConfig.models"), cap["model"])
		form = getattr(importlib.import_module("RaspNodeConfig.forms"), cap["form"])
	else:
		raise Http404('Capability not found')
	CapabilityFormset = modelformset_factory(model, form=form, can_delete=True)
	if request.method == 'POST':
		formset = CapabilityFormset(request.POST, queryset=model.objects.filter(node__exact=node_id))
		if formset.is_valid():
			instances = formset.save(commit=False)
			for instance in instances:
				instance.node = models.Node.objects.filter(id__exact = node_id).get()
				instance.save()
			for instance in formset.deleted_objects:
				instance.delete()
			return redirect('capability_form', room_id = room_id, node_id = node_id, capability = capability)
	else:
		# formset = CapabilityFormset(queryset=model.objects.filter(node__id__exact=node_id))
		formset = CapabilityFormset(queryset=model.objects.filter(node__exact=node_id))
	return render(request, 'capabilities.html', {'formset': formset})