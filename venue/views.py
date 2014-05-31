import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from arkansassymphony.venue.models import Venue
from django.http import HttpResponseRedirect

def venue_landing(request):
	masterworks_list = Venue.objects.filter(venue_type='masterworks', status='active')
	pops_list = Venue.objects.filter(venue_type='pops', status='active')
	chamber_list = Venue.objects.filter(venue_type='chamber', status='active')
	inc_list = Venue.objects.filter(venue_type='inc', status='active')
	other_list = Venue.objects.filter(venue_type='other', status='active')
	
	context = RequestContext(request)
	return render_to_response('venue/venue.html', {'masterworks_list': masterworks_list, 'pops_list': pops_list, 'chamber_list': chamber_list, 'inc_list': inc_list, 'other_list': other_list}, context_instance=context)
	
def venue_view(request, venue_url):
	venue_object = Venue.objects.get(url_name = venue_url)	

	#for left nav
	masterworks_list = Venue.objects.filter(venue_type='masterworks', status='active')
	pops_list = Venue.objects.filter(venue_type='pops', status='active')
	chamber_list = Venue.objects.filter(venue_type='chamber', status='active')
	inc_list = Venue.objects.filter(venue_type='inc', status='active')
	other_list = Venue.objects.filter(venue_type='other', status='active')
	
	context = RequestContext(request)
	return render_to_response('venue/venue_detail.html', {'venue_object': venue_object, 'masterworks_list': masterworks_list, 'pops_list': pops_list, 'chamber_list': chamber_list, 'inc_list': inc_list, 'other_list': other_list}, context_instance=context)
	#return render_to_response('venue/venue_detail.html', {'venue_object': venue_object}, context_instance=context)
