from django.shortcuts import render_to_response
from arkansassymphony.staff_board.models import Administrator
from django.template import RequestContext

def about(request):
	staff_list = Administrator.objects.filter(board_or_staff = 'staff').order_by('order')
	board_list = Administrator.objects.filter(board_or_staff = 'directors').order_by('order')
	advisor_list = Administrator.objects.filter(board_or_staff = 'advisors').order_by('order')
	
	return render_to_response('about/about.html', {'staff_list': staff_list, 'board_list': board_list, 'advisor_list': advisor_list}, context_instance=RequestContext(request))

def contactus(request):
	staff_list = Administrator.objects.filter(board_or_staff = 'staff').order_by('order')
	return render_to_response('connect/contactus.html', {'staff_list': staff_list}, context_instance=RequestContext(request))	
