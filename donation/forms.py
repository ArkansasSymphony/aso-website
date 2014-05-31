from django import forms
from django.forms import extras, ModelForm
from arkansassymphony.donation.models import *

class ModelDonationForm(ModelForm):
	
	class Meta:
		model = Donation
#		exclude = ('timestamp',)
