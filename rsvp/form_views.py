from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from arkansassymphony.rsvp.models import *

def RSVP_formview(request):
	from django import forms
	from arkansassymphony.rsvp.forms import ModelRSVPForm
	
	if request.method == 'POST':
		form = ModelRSVPForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zip = form.cleaned_data['zip']
			quantity = form.cleaned_data['quantity']
			notes = form.cleaned_data['notes']
			
			form.save()
			
			return render_to_response('rsvp/submitted.html', {'name': name, 'email': email, 'address': address, 'city': city, 'state': state, 'zip': zip, 'phone': phone, 'quantity': quantity, 'notes': notes}, context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelRSVPForm() #unbound form
		
	return render_to_response('rsvp/rsvp.html', {'form': form,}, context_instance=RequestContext(request))
