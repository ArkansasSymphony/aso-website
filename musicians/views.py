from django.shortcuts import render_to_response
from django.core.mail import send_mail
from arkansassymphony.musicians.models import *
from arkansassymphony.staff_board.models import Administrator
from django.template import RequestContext


def bus_info(request):
	current_season = "2013-2014"
	bus_list = Concert.objects.filter(season = current_season, bus_service = 'Yes').order_by('end_date')
	
	return render_to_response('musicians/bus-info.html', {'bus_list': bus_list, 'current_season': current_season}, context_instance=RequestContext(request))

def musician_portal(request):
	concert_doc = ConcertDocument.objects.get(name = 'musician_contact_doc')
	return render_to_response('musicians/musicians.html', {'concert_doc': concert_doc},  context_instance=RequestContext(request))
	
def information(request):
	return render_to_response('musicians/information.html', context_instance=RequestContext(request))
	
def concert_info(request):
	current_season = "2013-2014"
	concert_list = Concert.objects.filter(season = current_season).order_by('end_date')
	return render_to_response('musicians/concert-info.html', {'concert_list': concert_list, 'current_season': current_season}, context_instance=RequestContext(request))
	
def concert_view(request, concert_name):
	concert_object = Concert.objects.get(url_name = concert_name)
	service_list = Service.objects.filter(show__url_name = concert_name).order_by('date', 'time')
	pieceList = ProgramItem.objects.filter(show__name = concert_object.name).order_by('order')
	document_list = ConcertDocument.objects.filter(show__name = concert_object.name)
	
	return render_to_response('musicians/concert-view.html', {'concert_object': concert_object, 'service_list': service_list, 'pieceList': pieceList, 'document_list': document_list}, context_instance=RequestContext(request))

def venues(request):
	venue_list = Venue.objects.all()
	return render_to_response('musicians/venues.html', {'venue_list': venue_list}, context_instance=RequestContext(request))
	
def venue_detail(request, venue_url):
	venue_object = Venue.objects.get(url_name = venue_url)
	return render_to_response('musicians/venue_detail.html', {'venue_object': venue_object}, context_instance=RequestContext(request))
	
def wage_info(request):
	wage_list_current = WageChart.objects.filter(fiscal_year = '2013-14')
	return render_to_response('musicians/wage-chart.html', {'wage_list_current': wage_list_current}, context_instance=RequestContext(request))
	
def faq(request):
	wage_list_current = WageChart.objects.get(fiscal_year = '2013-14')
	return render_to_response('musicians/faq.html', {'wage_list_current': wage_list_current}, context_instance=RequestContext(request))
	
def info(request):
	return render_to_response('musicians/info.html', context_instance=RequestContext(request))
	
def ma_contents(request):
	ma_doc = ConcertDocument.objects.get(name="master_agreement_doc")
	return render_to_response('musicians/MA/ma-contents.html', {'ma_doc': ma_doc}, context_instance=RequestContext(request))
	
def ma(request, part):
	return render_to_response('musicians/MA/ma-%s.html' % part, context_instance=RequestContext(request))
	
def calendars(request):
	return render_to_response('musicians/calendars.html', context_instance=RequestContext(request))
	
def reservations(request):
	return render_to_response('musicians/reservations.html', context_instance=RequestContext(request))
	
def contact(request):
	concert_doc = ConcertDocument.objects.get(name = 'musician_contact_doc')
	return render_to_response('musicians/contact.html', {'concert_doc': concert_doc}, context_instance=RequestContext(request))
	
def forms(request):
	return render_to_response('musicians/forms.html', context_instance=RequestContext(request))
	
def hr(request):
	docs_list = HRDocument.objects.all()
	return render_to_response('musicians/hr.html', {'docs_list': docs_list}, context_instance=RequestContext(request))
	
def musician_forms(request):
	return render_to_response('musicians/musician-forms.html', context_instance=RequestContext(request))
	
def staff_contact(request):
	staff_list = Administrator.objects.filter(board_or_staff = 'staff')
	
	return render_to_response('musicians/staff-contact.html', {'staff_list': staff_list,}, context_instance=RequestContext(request))
