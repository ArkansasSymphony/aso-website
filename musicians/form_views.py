from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django import forms
from arkansassymphony.musicians.distance import main
from arkansassymphony.musicians.models import *
	
def thanks(request):
	return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request))
	
def byrne_form(request):
	from django import forms
	from arkansassymphony.musicians.forms import ByrneForm
	
	if request.method == 'POST':
		form = ByrneForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			date = form.cleaned_data['date']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			use = form.cleaned_data['use']
			multi = form.cleaned_data['multi']
			recipients = ['drenfro@arkansassymphony.org']
				
			from django.core.mail import send_mail
					
			recipients.append(email) #add user email address
			
			subject = 'FORM DATA: Byrne Hall Request'
			message = """
			The following request has been submitted:
			
			Request to reserve Byrne Hall
			
			Name - %s
			Email - %s
			Request date - %s
			Request start time - %s
			Request end time - %s
			Byrne Hall is being used for - %s
			Other - %s
			
			You will receive an email confirmation when your reservation is finalized.
			
			""" % (name, email, date, start_time, end_time, use, multi)
			
			send_mail(subject, message, email, recipients)
			
			return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ByrneForm() #unbound form
		
	return render_to_response('musicians/forms/byrne-request.html', {'form': form,}, context_instance=RequestContext(request))
	
def van_form(request):
	from django import forms
	from arkansassymphony.musicians.forms import VanForm
	
	if request.method == 'POST':
		form = VanForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			date = form.cleaned_data['date']
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			use = form.cleaned_data['use']
			multi = form.cleaned_data['multi']
			recipients = ['education@arkansassymphony.org']
				
			from django.core.mail import send_mail
					
			recipients.append(email) #add user email address
			
			subject = 'FORM DATA: Van Request'
			message = """
			The following request has been submitted:
			
			Request to reserve the ASO Van
			
			Name - %s
			Email - %s
			Request date - %s
			Request start time - %s
			Request end time - %s
			Van is being used for - %s
			Other - %s
			
			You will receive an email confirmation when your reservation is finalized.
			""" % (name, email, date, start_time, end_time, use, multi)
			
			send_mail(subject, message, email, recipients)
			
			
			return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = VanForm() #unbound form
		
	return render_to_response('musicians/forms/van-request.html', {'form': form,}, context_instance=RequestContext(request))
	
def bus_form(request, show_url):
	concert_object = Concert.objects.get(url_name = show_url)
	schedule = Schedule.objects.filter(show = concert_object).order_by("order")
	
	from django import forms
	from arkansassymphony.musicians.forms import ModelBusForm

	if request.method == 'POST':
		form = ModelBusForm(show_url, data=request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			riding = form.cleaned_data['riding']
			boarding = form.cleaned_data['boarding']
			meal = form.cleaned_data['meal']
			
			form.save()
			
			recipients = ['musicians@arkansassymphony.org']
				
			from django.core.mail import send_mail
					
			recipients.append(email) #add user email address
			
			subject = 'FORM DATA: Bus Request %s' % concert_object.name
			message = """
			The following request has been submitted:
			
			Request to ride ASO provided transportation
			
			Name - %s
			Email - %s
			Riding the bus - %s
			Boarding - %s
			Meal type - %s
			
			""" % (name, email, riding, boarding, meal)
			
			send_mail(subject, message, email, recipients)

			return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelBusForm(show_url) #unbound form
		
	return render_to_response('musicians/forms/bus-form.html', {'form': form, 'concert_object': concert_object, 'schedule': schedule}, context_instance=RequestContext(request))
			
			
def service_claim(request):
	wage_list_current = WageChart.objects.get(fiscal_year='2012-13')

	from django import forms
	from arkansassymphony.musicians.forms import AdminClaimForm
	
	if request.method == 'POST':
		form = AdminClaimForm(request.POST)
		if form.is_valid():
			form_type = form.cleaned_data['form_type']
			name = form.cleaned_data['name']
			service = form.cleaned_data['service']
			other_service = form.cleaned_data['other_service']
			email = form.cleaned_data['email']
			leg1a = form.cleaned_data['leg1a']
			leg1b = form.cleaned_data['leg1b']
			leg2a = form.cleaned_data['leg2a']
			leg2b = form.cleaned_data['leg2b']
			leg3a = form.cleaned_data['leg3a']
			leg3b = form.cleaned_data['leg3b']
			leg4a = form.cleaned_data['leg4a']
			leg4b = form.cleaned_data['leg4b']
			leg5a = form.cleaned_data['leg5a']
			leg5b = form.cleaned_data['leg5b']
			leg6a = form.cleaned_data['leg6a']
			leg6b = form.cleaned_data['leg6b']
			date1 = form.cleaned_data['date1']
			date2 = form.cleaned_data['date2']
			date3 = form.cleaned_data['date3']
			date4 = form.cleaned_data['date4']
			date5 = form.cleaned_data['date5']
			date6 = form.cleaned_data['date6']
			round1 = form.cleaned_data['round1']
			round2 = form.cleaned_data['round2']
			round3 = form.cleaned_data['round3']
			round4 = form.cleaned_data['round4']
			round5 = form.cleaned_data['round5']
			round6 = form.cleaned_data['round6']
			principal_instrument = form.cleaned_data['principal_instrument']
			double_1 = form.cleaned_data['double_1']
			double_2 = form.cleaned_data['double_2']
			double_3 = form.cleaned_data['double_3']
			double_4 = form.cleaned_data['double_4']
			service_number = form.cleaned_data['service_number']
			cartage = form.cleaned_data['cartage']
			diem_type = form.cleaned_data['diem_type']
			comments = form.cleaned_data['comments']
			
			#convert unicode data to strings for clean email output		
			
			cartage_out = [str(x) for x in cartage] #uncomment to use form instead of ModelForm
			#for i in service:       uncomment to use form instead of ModelForm
			#	service = i.name     uncomment to use form instead of ModelForm
			
			leg1b = leg1b.encode('latin-1')
			leg2a = leg2a.encode('latin-1')
			leg2b = leg2b.encode('latin-1')
			leg3a = leg3a.encode('latin-1')
			leg3b = leg3b.encode('latin-1')
			leg4a = leg4a.encode('latin-1')
			leg4b = leg4b.encode('latin-1')
			leg5a = leg5a.encode('latin-1')
			leg5b = leg5b.encode('latin-1')
			leg6a = leg6a.encode('latin-1')
			leg6b = leg6b.encode('latin-1')
			
			form.save()
			
		
			#Mileage distance calculation			
			leg_list = [(leg1a, leg1b), (leg2a, leg2b), (leg3a, leg3b), (leg4a, leg4b), (leg5a, leg5b), (leg6a, leg6b)]
			
			if round1 == True:
				leg_list.append((leg1a, leg1b))
			if round2 == True:
				leg_list.append((leg2a, leg2b))
			if round3 == True:
				leg_list.append((leg3a, leg3b))
			if round4 == True:
				leg_list.append((leg4a, leg4b))
			if round5 == True:
				leg_list.append((leg5a, leg5b))
			if round6 == True:
				leg_list.append((leg6a, leg6b))

			cleaned_leg_list = []
			#get rid of empty variables
			for leg in leg_list:
				if leg == ('',''):
					pass
				else:
					cleaned_leg_list.append(leg)
			leg_distance = []

			#sends each leg of mileage claim to distance handler
			for leg in cleaned_leg_list:
				pre_leg = main(leg)
				leg_distance.append(pre_leg)
			#sums legs of mileage claim	
			mileage_miles = sum(leg_distance)
			

			#mileage_miles = "Will be calculated"
			#mileage_paid = "Will be calculated"

			#tally claim amount
			doubles = [double_1, double_2, double_3, double_4]
			doubling_paid = 0
			for i in doubles:
				if i == "":
					pass
				else:
					doubling_paid += wage_list_current.doubling
			if service_number == None:
				doubling_paid = 0
			else:
				doubling_paid = doubling_paid * service_number
			
			if cartage == [u'']:
				cartage_paid = 0
			else:
				cartage_count = len(cartage)
				cartage_paid = 0
				if 'Marimba' in cartage:
					cartage_paid += wage_list_current.marimba_cartage
					cartage_count = cartage_count - 1
				if 'Vibes' in cartage:
					cartage_paid += wage_list_current.vibes_cartage
					cartage_count = cartage_count - 1
				cartage_paid += cartage_count * wage_list_current.standard_cartage
		
			if diem_type == [u'']:	
				diem_paid = 0
			else:
				diem_paid = 0
				for diem in diem_type:
					if diem == 'Quartet only - breakfast':
						diem_paid += wage_list_current.breakfast
					if diem == 'Quartet only - lunch':
						diem_paid += wage_list_current.lunch
					if diem == 'Quartet only - dinner':
						diem_paid += wage_list_current.dinner
					if diem == 'Single performance':
						diem_paid += wage_list_current.per_diem_single
					if diem == 'Double performance':
						diem_paid += wage_list_current.per_diem_double
				
			mileage_paid = mileage_miles * wage_list_current.mileage
			
			claim_total = doubling_paid + cartage_paid + diem_paid + mileage_paid
			
			#send email to appropriate department
			if form_type == "Standard":
				recipients = ['drenfro@arkansassymphony.org']
			elif form_type == "Quartet/Chamber/Outreach":
				recipients = ['bburroughs@arkansassymphony.org', 'education@arkansassymphony.org']
			
			recipients.append(email)
			
			from django.core.mail import send_mail
		
			if other_service == "":
			
				subject = 'FORM DATA: Service Claim'
				message = """
			
				Service Claim submitted as follows:
			
				Name - %s
				Service - %s
				Email - %s
			
				Mileage - Miles: %s  Mileage claim: %s
			
				Leg 1: %s
				Leg 2: %s
				Leg 3: %s
				Leg 4: %s
				Leg 5: %s
				Leg 6: %s
			
				**Doubling**
			
				Principal Instrument - %s
				Double 1 - %s
				Double 2 - %s
				Double 3 - %s
				Double 4 - %s
				Number of Services - %s
				Doubling paid - $%s
			
				**Cartage**
			
				Cartage - %s
				Cartage paid -$%s
			
				**Other**
			
				Per diem - %s, $%s
			
				Claim total - $%s + mileage
			
				Comments - %s
		
				""" % (name, service, email, mileage_miles, mileage_paid, leg_list[0], leg_list[1], leg_list[2], leg_list[3], leg_list[4], leg_list[5], principal_instrument, double_1, double_2, double_3, double_4, service_number, doubling_paid, cartage_out, cartage_paid, diem_type, diem_paid, claim_total, comments)
				send_mail(subject, message, email, recipients)

			else:
				subject = 'FORM DATA: Service Claim'
				message = """
			
				Service Claim submitted as follows:
			
				Name - %s
				Service - %s
				Email - %s
				
				Mileage - %s miles, $%s
			
				Leg 1: %s
				Leg 2: %s
				Leg 3: %s
				Leg 4: %s
				Leg 5: %s
				Leg 6: %s
			
				**Doubling**
			
				Principal Instrument - %s
				Double 1 - %s
				Double 2 - %s
				Double 3 - %s
				Double 4 - %s
				Number of Services - %s
				Doubling paid - $%s
				
				**Cartage**
			
				Cartage - %s
				Cartage paid -$%s
			
				**Other**
			
				Per diem - %s, $%s
			
				Claim total - $%s + mileage
			
				Comments - %s
		
				""" % (name, other_service, email, mileage_miles, mileage_paid, leg_list[0], leg_list[1], leg_list[2], leg_list[3], leg_list[4], leg_list[5], principal_instrument, double_1, double_2, double_3, double_4, service_number, doubling_paid, cartage_out, cartage_paid, diem_type, diem_paid, claim_total, comments)
			
				send_mail(subject, message, email, recipients)
			
			return render_to_response('musicians/forms/submitted.html', {'name': name, 'service': service,'mileage_miles': mileage_miles, 'mileage_paid': mileage_paid, 'doubling_paid': doubling_paid, 'cartage_paid': cartage_paid, 'diem_paid': diem_paid, 'claim_total': claim_total, 'comments': comments}, context_instance=RequestContext(request)) #redirect after POST
	else:
		form = AdminClaimForm() #unbound form
		
	return render_to_response('musicians/forms/service-claim.html', {'form': form, 'wage_list_current': wage_list_current}, context_instance=RequestContext(request))	
	
def comp_request(request):
	from django import forms
	from arkansassymphony.musicians.forms import CompForm
	
	if request.method == 'POST':
		form = CompForm(request.POST)
		if form.is_valid():
			musician_name = form.cleaned_data['musician_name']
			show = form.cleaned_data['show']
			email = form.cleaned_data['email']
			day = form.cleaned_data['day']
			quantity = form.cleaned_data['quantity']
			notes = form.cleaned_data['notes']
			delivery = form.cleaned_data['delivery']

			form.save()
		
			recipients = ['bdorris@arkansassymphony.org']
	
			from django.core.mail import send_mail

			subject = "Comp ticket request"
			message = """
				Your comp ticket request has been received as follows:
				
				name = %s
				concert = %s, %s
				quantity = %r
				deliver = %s
				notes = %s

				Please contact the Box Office if you have any questions or need to make a change.

			""" % (musician_name, day, show, quantity, delivery, notes)
			
			recipients.append(email)

			send_mail(subject, message, email, recipients)
								
			return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = CompForm() #unbound form
		
	return render_to_response('musicians/forms/comp-request.html', {'form': form,}, context_instance=RequestContext(request))
	
def hotel_request(request):
	from django import forms
	from arkansassymphony.musicians.forms import ModelHotelForm
	
	if request.method == 'POST':
		form = ModelHotelForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			check_in = form.cleaned_data['check_in']
			check_out = form.cleaned_data['check_out']
			room_type = form.cleaned_data['room_type']
			roommate_request = form.cleaned_data['roommate_request']
			
			form.save()
			
			recipients = ['drenfro@arkansassymphony.org']
				
			from django.core.mail import send_mail
					
			recipients.append(email) #add user email address
					
			subject = 'FORM DATA: Hotel Request'
			message = """
			
			Claim submitted as follows:
			
			Name - %s
			Check-in Date - %s
			Check-out Date - %s
			Email - %s
			Single or double - %s
			Roommate request - %s
		
			""" % (name, check_in, check_out, email, room_type, roommate_request)
			
			send_mail(subject, message, email, recipients)
			
			return render_to_response('musicians/forms/thanks.html', context_instance=RequestContext(request)) #redirect after POST
	else:
		form = ModelHotelForm() #unbound form
		
	return render_to_response('musicians/forms/hotel-request.html', {'form': form,}, context_instance=RequestContext(request))
	
