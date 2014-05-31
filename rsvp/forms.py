from django import forms
from django.forms import extras, ModelForm
from arkansassymphony.rsvp.models import *

class ModelRSVPForm(ModelForm):
	
	class Meta:
		model = RSVP