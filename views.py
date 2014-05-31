import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from arkansassymphony.concerts.models import Show
from arkansassymphony.sponsors.models import Sponsor
from arkansassymphony.comments.models import Comment
from arkansassymphony.forms import LoyaltyForm
from django.http import HttpResponseRedirect


def mainPage(request):
	showList = Show.objects.filter(end_date__gte= datetime.date.today()).exclude(type='nutcracker').order_by('end_date', 'id')[:5]

	
	context = RequestContext(request)
	return render_to_response('index.html', {'showList': showList}, context_instance=context)

def season(request):
	mwList = Show.objects.filter(type='classical', season='2014-2015').order_by('end_date')
	popsList = Show.objects.filter(type='pops', season='2014-2015').order_by('end_date')
	chamberList = Show.objects.filter(type='chamber', season='2014-2015').order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('special/season.html', {'mwList': mwList, 'popsList': popsList, 'chamberList': chamberList}, context_instance=context)


def pick2(request):
	mwList = Show.objects.filter(type='classical', season='2014-2015').order_by('end_date')
	popsList = Show.objects.filter(type='pops', season='2014-2015').order_by('end_date')
	chamberList = Show.objects.filter(type='chamber', season='2014-2015').order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('special/pick2.html', {'mwList': mwList, 'popsList': popsList, 'chamberList': chamberList}, context_instance=context)

def pick2guild(request):
	mwList = Show.objects.filter(type='classical', season='2011-2012').order_by('end_date')
	popsList = Show.objects.filter(type='pops', season='2011-2012').order_by('end_date')
	chamberList = Show.objects.filter(type='chamber', season='2011-2012').order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('special/pick2guild.html', {'mwList': mwList, 'popsList': popsList, 'chamberList': chamberList}, context_instance=context)


def loyalty(request):
	if request.method == 'POST':
		form = LoyaltyForm(request.POST)
		if form.is_valid():
			file = open('/workspace/arkansassymphony/loyalty.csv', 'a')
			file.write('"%(name)s","%(email)s","%(years)s","%(improve)s","%(favorite)s"' % {'name': form.cleaned_data['name'], 'email': form.cleaned_data['email'], 'years': form.cleaned_data['yearsSubscribed'], 'improve': form.cleaned_data['improve'], 'favorite': form.cleaned_data['favorite']})
			file.close()

			return HttpResponseRedirect('/thanks/')
	else:
		form = LoyaltyForm()

	return render_to_response('loyalty.html', {'form': form})
