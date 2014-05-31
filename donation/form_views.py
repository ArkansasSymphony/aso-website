from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django import forms
from arkansassymphony.donation.models import *
import stripe

def donation_formview(request):
	from django import forms
	from arkansassymphony.donation.forms import ModelDonationForm
	stripe.api_key = "sk_live_5Sj3N6Pw2s9VlTvrDBfkKKh2" #live secret key
	#stripe.api_key = "sk_test_LzACjJeSISN4levLs9PkYRTY" #test secret key
	
	if request.method == 'POST':
		form = ModelDonationForm(request.POST)

		token = request.POST['stripeToken'] #passed from stripe.js to keep card info off this server

		if form.is_valid():
			name = form.cleaned_data['name']
			donation = form.cleaned_data['donation']
			anonymous = form.cleaned_data['anonymous']
			email = form.cleaned_data['email']
			phone = form.cleaned_data['phone']
			address = form.cleaned_data['address']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zip = form.cleaned_data['zip']
			notes = form.cleaned_data['notes']
			#timestamp = form.cleaned_data['timestamp']
			
			# Create the charge on Stripe's servers - this will charge the user's card
			charge = stripe.Charge.create(
				amount = donation*100, # convert dollars to cents
				currency = "usd",
				card = token,
				description = email
			)
			if anonymous == "Yes":
				anonymous = "No"
			elif anonymous == "No":
				anonymous == "Yes"
			
			#timestamp = timezone.now()

			form.save()
			
			#gather partial card info for email to Development
			card_type = charge['card'].type
			last_four = charge['card'].last4
			card_month = str(charge['card'].exp_month)
			card_year = str(charge['card'].exp_year)


			from django.core.mail import send_mail
			recipients = ['bflynn@arkansassymphony.org', 'ahall@arkansassymphony.org']
			#recipients = ['bdorris@arkansassymphony.org']
			
			subject = 'ONLINE DONATION RECEIVED'
			message = """
			
			An online gift was processed as follows:
			
			%s
			%s
			%s
			%s, %s %s
			%s
			
			Donation amount: $ %s
			Anonymous: %s
			Card: "%s ********%s %s/%s"
			Notes: %s
			
			""" % (name, email, address, city, state, zip, phone, str(donation), anonymous, card_type, last_four, card_month, card_year, notes)
			
			send_mail(subject, message, email, recipients)
			
			return render_to_response('donation/submitted.html', {'name': name, 'email': email, 'address': address, 'city': city, 'state': state, 'zip': zip, 'phone': phone, 'donation': donation, 'anonymous': anonymous, 'notes': notes}, context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelDonationForm() #unbound form
		
	return render_to_response('donation/donate.html', {'form': form,}, context_instance=RequestContext(request))
