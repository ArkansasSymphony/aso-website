from arkansassymphony.checkin.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
import stripe

def go(request, id):
	#stripe.api_key = "sk_test_LzACjJeSISN4levLs9PkYRTY"
	stripe.api_key = "sk_live_5Sj3N6Pw2s9VlTvrDBfkKKh2"

	id_process = Patron.objects.get(id=id)
	if id_process.cc_number != "None":		
		customer_create = stripe.Customer.create(
		card = {
			"number": id_process.cc_number, 
			"exp_month": id_process.cc_month, 
			"exp_year": id_process.cc_year, 
			"cvc": id_process.cc_cvc, 
			"name": id_process.full_name, 
			"address_line1": id_process.address, 
			"address_zip": id_process.zip, 
			"address_state": id_process.state
		},
		email = id_process.email

		)
		
		
		customer = Patron.objects.get(full_name = id_process.full_name)
		customer.stripe_id = customer_create.id
		customer.cc_number = "STRIPE STORED"
		customer.cc_month = 99
		customer.cc_year = 9999
		customer.cc_cvc = "STRIPE STORED"
		
		customer.save()
	else:
		customer = Patron.objects.get(full_name = id_process.full_name)
		customer.cc_number = "NOT STORED"
		customer.save()
		
	return render_to_response('checkin/admin/go.html', {'id_process': id_process}, context_instance=RequestContext(request))
	
go = staff_member_required(go)
