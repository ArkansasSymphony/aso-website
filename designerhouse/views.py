from arkansassymphony.designerhouse.models import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def designer_main(request):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')

	return render_to_response('designerhouse/designer-main.html', {'sponsor_list': sponsor_list}, context_instance=RequestContext(request))

def about_view(request):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')
	return render_to_response('designerhouse/designer-about.html', {'sponsor_list': sponsor_list}, context_instance=RequestContext(request))

def sponsor_view(request):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')

	return render_to_response('designerhouse/designer-sponsor.html', {'sponsor_list': sponsor_list}, context_instance=RequestContext(request))

def designer_view(request):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')
	designer_list = Designer.objects.all()

	return render_to_response('designerhouse/designer-designer.html', {'designer_list': designer_list, 'sponsor_list': sponsor_list}, context_instance=RequestContext(request))

def tickets_view(request):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')
	
	return render_to_response('designerhouse/designer-tickets.html', {'sponsor_list': sponsor_list}, context_instance=RequestContext(request))

def party_view(request, party_url):
	sponsor_list = Sponsor.objects.all().order_by('sponsor_name')
	parties_list = Party.objects.filter(url_name = party_url)
	for i in parties_list:
		party_object = i

	return render_to_response('designerhouse/designer-party.html', {'parties_list': parties_list, 'party_object': party_object, 'sponsor_list': sponsor_list}, context_instance=RequestContext(request))
