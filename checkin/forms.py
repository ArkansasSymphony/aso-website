from django import forms
from django.forms import extras, ModelForm
from arkansassymphony.checkin.models import *

class ModelPatronForm(ModelForm):
	class Meta:
		model = Patron
		
class ModelChargeForm(ModelForm):
	class Meta:
		model = Charge
		
"""class ModelPatronForm(forms.Form):
	name = forms.CharField(max_length=100, required = True)
	email = forms.EmailField()
	cc_number = forms.CharField(max_length = 100, required = False)
	cc_month = forms.IntegerField(required = False)
	cc_year = forms.IntegerField(required = False)
	cc_cvc = forms.CharField(max_length = 4, required = False)
	stripe_id = forms.CharField(max_length=100, required = False)
	phone = forms.CharField(max_length=100, required = False)
	address = forms.CharField(max_length=100, required = False)
	city = forms.CharField(max_length=100, required = False)
	state = forms.CharField(max_length=2, required = False)
	zip = forms.CharField(max_length=100, required = False)
	dining_assignment = forms.CharField(max_length=100, required = False)
	notes = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)"""