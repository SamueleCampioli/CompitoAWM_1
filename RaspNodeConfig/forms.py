from django.forms import ModelForm
from . import models


class RoomForm(ModelForm):
	class Meta:
		model = models.Room
		fields = ['id', 'name', 'user']
		exclude = ['user']

class NodeForm(ModelForm):
    class Meta:
        model = models.Node
        fields = ['id', 'name', 'user', 'room']
        exclude = ['user', 'room']


class TapparelleCapabilityForm(ModelForm):
	class Meta:
		model = models.TapparelleCapabilityEntry
		fields = ['id', 'name', 'descrizione', 'node', 'pinUp', 'pinDown', 'timeout']
		exclude = ['node']


class TemperaturaCapabilityForm(ModelForm):
	class Meta:
		model = models.TemperaturaCapabilityEntry
		fields = ['id', 'name', 'descrizione', 'node', 'pin', 'sensor', 'update']
		exclude = ['node']


class SwitchCapabilityForm(ModelForm):
	class Meta:
		model = models.SwitchCapabilityEntry
		fields = ['id', 'name', 'descrizione', 'node', 'pin']
		exclude = ['node']


class ButtonCapabilityForm(ModelForm):
	class Meta:
		model = models.ButtonCapabilityEntry
		fields = ['id', 'name', 'descrizione', 'node', 'pin', 'topic']
		exclude = ['node']
