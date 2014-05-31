from arkansassymphony.musicians.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from arkansassymphony.musicians.distance import main, state_fix


def report(request):
	wage_list_current = WageChart.objects.get(fiscal_year='2012-13')
	service_claim_list = AdminClaimForm.objects.all()
	
	for claim in service_claim_list:
	
		claim.leg1a = state_fix(claim.leg1a)
		claim.leg1b = state_fix(claim.leg1b)
		claim.leg2a = state_fix(claim.leg2a)
		claim.leg2b = state_fix(claim.leg2b)
		claim.leg3a = state_fix(claim.leg3a)
		claim.leg3b = state_fix(claim.leg3b)
		claim.leg4a = state_fix(claim.leg4a)
		claim.leg4b = state_fix(claim.leg4b)
		claim.leg5a = state_fix(claim.leg5a)
		claim.leg5b = state_fix(claim.leg5b)
		claim.leg6a = state_fix(claim.leg6a)
		claim.leg6b = state_fix(claim.leg6b)


		#Mileage distance calculation			
		leg_list = [(claim.leg1a, claim.leg1b), (claim.leg2a, claim.leg2b), (claim.leg3a, claim.leg3b), (claim.leg4a, claim.leg4b), (claim.leg5a, claim.leg5b), (claim.leg6a, claim.leg6b)]
	
		
		if claim.round1 == True:
			leg_list.append((claim.leg1a, claim.leg1b))
		if claim.round2 == True:
			leg_list.append((claim.leg2a, claim.leg2b))
		if claim.round3 == True:
			leg_list.append((claim.leg3a, claim.leg3b))
		if claim.round4 == True:
			leg_list.append((claim.leg4a, claim.leg4b))
		if claim.round5 == True:
			leg_list.append((claim.leg5a, claim.leg5b))
		if claim.round6 == True:
			leg_list.append((claim.leg6a, claim.leg6b))

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
			leg_distance.append(main(leg))
		#sums legs of mileage claim	
		sum_distance = sum(leg_distance)
		
		#tally claim amount
		doubles = [claim.double_1, claim.double_2, claim.double_3, claim.double_4]
		doubling_paid = 0
		for i in doubles:
			if i == "":
				pass
			else:
				doubling_paid += wage_list_current.doubling
		if claim.service_number == None:
			doubling_paid = 0
		else:
			doubling_paid = doubling_paid * claim.service_number
	
	
		if claim.cartage == [u'']:
				cartage_paid = 0

		else:
			cartage_paid = 0
			cartage_list = []
			for i in claim.cartage:
				cartage_list.append(i)
			for i in cartage_list:
				if i == 'Marimba':
					cartage_paid += wage_list_current.marimba_cartage
				if i == 'Vibes':
					cartage_paid += wage_list_current.vibes_cartage
				else:
					cartage_paid += wage_list_current.standard_cartage
	
		if claim.diem_type == [u'']:
			diem_paid = 0
		else:
			diem_paid = 0
			for diem in claim.diem_type:
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
		
		mileage_paid = sum_distance * wage_list_current.mileage
		
		claim_total = doubling_paid + cartage_paid + diem_paid + mileage_paid
		claim.mileage_miles = sum_distance
		claim.mileage_claim = mileage_paid
		claim.doubling_claim = doubling_paid
		claim.cartage_claim = cartage_paid
		claim.diem_claim = diem_paid
		claim.total_claim = claim_total
		claim.save()
						
	return render_to_response('musicians/admin/report.html', {'service_claim_list': service_claim_list}, context_instance=RequestContext(request))
	
report = staff_member_required(report)
