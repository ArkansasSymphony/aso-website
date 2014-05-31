from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from arkansassymphony.jobs.models import Job


def jobsMain(request):
	orchList = Job.objects.filter(active=True).filter(type='orchestra').order_by('title')
	adminList = Job.objects.filter(active=True).filter(type='admin').order_by('title')	
	
	return render_to_response('about/jobs.html', {'orchList': orchList, 'adminList': adminList}, 
context_instance=RequestContext(request))



def jobDetail(request, jobTitle):
	try:
		job = Job.objects.get(url_name=jobTitle, active=True)
	except ObjectDoesNotExist:
		return HttpResponseRedirect(reverse('jobsMain'))

	return render_to_response('about/job_detail.html', {'job': job}, context_instance=RequestContext(request))
