from django import forms
from django.forms import extras, ModelForm
from arkansassymphony.musicians.models import *

class ByrneForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	date = forms.DateField()
	start_time = forms.CharField(max_length=20)
	end_time = forms.CharField(max_length=20)
	use = forms.CharField(max_length=500, widget=forms.Textarea)
	multi = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)
	
class VanForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()
	date = forms.DateField()
	start_time = forms.CharField(max_length=20)
	end_time = forms.CharField(max_length=20)
	use = forms.CharField(max_length=500, widget=forms.Textarea)
	multi = forms.CharField(max_length=1000, widget=forms.Textarea, required=False)
	
class AdminClaimForm(ModelForm):
	class Meta:
		model = AdminClaimForm

	def __init__(self, *args, **kwargs):
		super(AdminClaimForm, self).__init__(*args, **kwargs)
		self.fields['service'].queryset = Concert.objects.order_by('end_date')


class CompForm(ModelForm):
	class Meta:
		model = CompTicket
	
	def __init__(self, *args, **kwargs):
		super(CompForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['show'].queryset = Concert.objects.filter(comps_available = "Yes").order_by("end_date")
			
class ModelBusForm(ModelForm):
	class Meta:
		model = BusForm
	
	def __init__(self, show_url, *args, **kwargs):
		super(ModelBusForm, self).__init__(*args, **kwargs)
		if self.instance:
			self.fields['boarding'].queryset = BusStop.objects.filter(show__url_name=show_url).order_by('id')	
		#	self.fields['show'].queryset = Concert.objects.filter(url_name=show_url)
	def __unicode__(self):
		return self.name
			
class ModelHotelForm(ModelForm):
	class Meta:
		model = HotelForm
