

def pre_distance():
	leg_list = [(claim.leg1a, claim.leg1b), (claim.leg2a, claim.leg2b), (claim.leg3a, claim.leg3b), (claim.leg4a, claim.leg4b), (claim.leg5a, claim.leg5b), (claim.leg6a, claim.leg6b)]
		
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
		sum_distance = sum(leg_distance)
		
		#tally claim amount
		doubles = [claim.double_1, claim.double_2, claim.double_3, claim.double_4]
		doubling_paid = 0
		for i in doubles:
			if i == "":
				pass
			else:
				doubling_paid += wage_list_current.doubling
		if claim.service_number == "":
			doubling_paid = 0
		else:
			doubling_paid = doubling_paid * claim.service_number
		
		if claim.cartage == None:
				cartage_paid = 0
		else:
			cartage_count = len(claim.cartage)
			cartage_paid = 0
			if 'Marimba' in claim.cartage:
				cartage_paid += wage_list_current.marimba_cartage
				cartage_count = cartage_count - 1
			if 'Vibes' in claim.cartage:
				cartage_paid += wage_list_current.vibes_cartage
				cartage_count = cartage_count - 1
			cartage_paid += cartage_count * wage_list_current.standard_cartage
		
		diem_paid = 0
		if claim.diem_type == 'Single performance':
			diem_paid += wage_list_current.per_diem_single
		if claim.diem_type == 'Double performance':
			diem_paid += wage_list_current.per_diem_double
			
		mileage_paid = sum_distance * wage_list_current.mileage
		
		claim_total = doubling_paid + cartage_paid + diem_paid + mileage_paid