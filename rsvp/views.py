from django.shortcuts import render_to_response
from arkansassymphony.rsvp.models import *
from django.template import RequestContext


def rsvp_info(request):
	rsvp_data = RSVP.objects.all()
	rsvp_count = 0
	for i in rsvp_data:
		rsvp_count = rsvp_count + i.quantity
	
	return render_to_response('rsvp/rsvp-info.html', {'rsvp_count': rsvp_count,}, context_instance=RequestContext(request))
