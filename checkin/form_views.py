from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django import forms
from arkansassymphony.checkin.models import *
import stripe

def patron_formview(request):
	from django import forms
	from arkansassymphony.checkin.forms import ModelPatronForm
	#stripe.api_key = "sk_test_LzACjJeSISN4levLs9PkYRTY"
	stripe.api_key = "sk_live_5Sj3N6Pw2s9VlTvrDBfkKKh2"
	
	if request.method == 'POST':
		form = ModelPatronForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			full_name = form.cleaned_data['full_name']
			email = form.cleaned_data['email']
			organization = form.cleaned_data['organization']
			bid_number = form.cleaned_data['bid_number']
			cc_number = form.cleaned_data['cc_number']
			cc_month = form.cleaned_data['cc_month']
			cc_year = form.cleaned_data['cc_year']
			cc_cvc = form.cleaned_data['cc_cvc']
			stripe_id = form.cleaned_data['stripe_id']
			phone = form.cleaned_data['phone']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zip = form.cleaned_data['zip']
			dining_assignment = form.cleaned_data['dining_assignment']
			notes = form.cleaned_data['notes']
			
			form.save()
			
			if cc_number != "None":		
				customer_create = stripe.Customer.create(
				card = {
					"number": cc_number, 
					"exp_month": cc_month, 
					"exp_year": cc_year, 
					"cvc": cc_cvc, 
					"name": full_name, 
					"address_line1": address, 
					"address_zip": zip, 
					"address_state": state
				},
				email = email
			
				)
				
				
				customer = Patron.objects.get(full_name = full_name)
				customer.stripe_id = customer_create.id
				customer.cc_number = "STRIPE STORED"
				customer.cc_month = 99
				customer.cc_year = 9999
				customer.cc_cvc = "STRIPE STORED"
				
				customer.save()
			else:
				customer = Patron.objects.get(full_name = full_name)
				customer.cc_number = "NOT STORED"
				customer.save()

			return render_to_response('checkin/submitted.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelPatronForm() #unbound form
		
	return render_to_response('checkin/checkin.html', {'form': form,}, context_instance=RequestContext(request))
	
def charge_formview(request):
	from django import forms
	from arkansassymphony.checkin.forms import ModelChargeForm
	#stripe.api_key = "sk_test_LzACjJeSISN4levLs9PkYRTY"
	stripe.api_key = "sk_live_5Sj3N6Pw2s9VlTvrDBfkKKh2"
	
	if request.method == 'POST':
		form = ModelChargeForm(request.POST)
		if form.is_valid():
			description = form.cleaned_data['description']
			price = form.cleaned_data['price']
			customer = form.cleaned_data['customer']
			payment_method = form.cleaned_data['payment_method']
			notes = form.cleaned_data['notes']
			
			form.save()
			
			if payment_method == "Card":
			
				cents = price * 100
				results = stripe.Charge.create(
					amount = cents,
					currency = "usd",
					customer = customer.stripe_id,
					description = description
				)
				
				return render_to_response('checkin/charge-submitted.html', context_instance=RequestContext(request)) #redirect after POST
				
			else:
				return render_to_response('checkin/charge-submitted.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelChargeForm() #unbound form
		
	return render_to_response('checkin/charge.html', {'form': form,}, context_instance=RequestContext(request))
