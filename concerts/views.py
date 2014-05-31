import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from arkansassymphony.concerts.models import Show, Concert, Subscription, Piece
from arkansassymphony.people.models import Artist
from arkansassymphony.multimedia.models import Music, Video


def concertsPage(request, display, season):
	if display == "all":
		showList = Show.objects.filter(season=season).exclude(type='nutcracker').order_by('end_date')
	else:
		showList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(season=season).exclude(type='nutcracker').order_by('end_date')
	
	
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'showList': showList, 'display': display, 'category': 'all', 'season': season}, context_instance=context)



def showDetail(request, urlName):
	concertList = Concert.objects.filter(show__url_name = '%s' % urlName).extra(select={'is_past': "SELECT 'False'"}).order_by('date')
	pieceList = Piece.objects.filter(show = concertList[0].show)

	callBoxOffice = False
	for concert in concertList:
		if concert.date < datetime.datetime.now():
			concert.is_past = "True"
		if concert.pe_id == 248:
			callBoxOffice = True

	context = RequestContext(request)
	return render_to_response('concerts/concert_detail.html', {'concertList': concertList, 'show': concertList[0].show, 
'pieceList': pieceList, 'callBoxOffice': callBoxOffice}, 
context_instance=context)


def subscriptionPage(request):
	subList = Subscription.objects.all()
		
	context = RequestContext(request)
	return render_to_response('concerts/subscriptions.html', {'subList': subList}, context_instance=context)


def mwPage(request, display, season):
	if display == "all":
		mwList = Show.objects.filter(type='classical').filter(season=season).order_by('end_date')
	else:
		mwList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(type='classical').filter(season=season).order_by('end_date')
	
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'mwList': mwList, 'display': display, 'category': 'masterworks', 'season': season}, context_instance=context)


def popsPage(request, display, season):
	if display == "all":
		popsList = Show.objects.filter(type='pops').filter(season=season).order_by('end_date')
	else:
		popsList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(type='pops').filter(season=season).order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'popsList': popsList, 'display': display, 'category': 'pops', 'season': season}, context_instance=context)


def chamberPage(request, display, season):
	if display == "all":
		chamberList = Show.objects.filter(type='chamber').filter(season=season).order_by('end_date')
	else:
		chamberList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(type='chamber').filter(season=season).order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'chamberList': chamberList, 'display': display, 'category': 'chamber', 'season': season}, context_instance=context)

def neighborhoodPage(request, display, season):
	if display == "all":
		neighborhoodList = Show.objects.filter(type='neighborhood').filter(season=season).order_by('end_date')
	else:
		neighborhoodList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(type='neighborhood').filter(season=season).order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'neighborhoodList': neighborhoodList, 'display': display, 'category': 'neighborhood', 'season': season}, context_instance=context)

def otherPage(request, display, season):
	if display == "all":
		otherLis = Show.objects.filter(type='other').filter(season=season).order_by('end_date')
	else:
		otherList = Show.objects.filter(end_date__gte= datetime.date.today()).filter(type='other').filter(season=season).order_by('end_date')
		
	context = RequestContext(request)
	return render_to_response('concerts/concerts.html', {'otherList': otherList, 'display': display, 'category': 'other', 'season': season}, context_instance=context)

def noteDetail(request, urlName, showUrlName):
	pieceList = Piece.objects.filter(url_name = '%s' % urlName)
		
	context = RequestContext(request)
	return render_to_response('themusic/note_detail.html', {'piece': pieceList[0]}, context_instance=context)


def notePage(request, sortBy):
	if sortBy == "composer":
		pieceList = Piece.objects.all().order_by('composer')
	else:
		pieceList = Piece.objects.all().order_by('title')
		
	context = RequestContext(request)
	return render_to_response('themusic/notes.html', {'pieceList': pieceList, 'sortBy': sortBy}, context_instance=context)


	
def artistPage(request, urlName, showUrlName):
	artistList = Artist.objects.filter(url_name = '%s' % urlName)
	showList = Show.objects.filter(url_name = '%s' % showUrlName)
		
	context = RequestContext(request)
	return render_to_response('concerts/artists.html', {'artist': artistList[0], 'show': showList[0]}, context_instance=context)
	

def freeKids(request):
	mwList = Show.objects.filter(type='classical').filter(end_date__gte= datetime.date.today()).filter(season='2013-2014').order_by('end_date')
	popsList = Show.objects.filter(type='pops').filter(end_date__gte= datetime.date.today()).filter(season='2013-2014').order_by('end_date')
	
	context = RequestContext(request)
	return render_to_response('education/freekids.html', {'mwList': mwList, 'popsList': popsList}, context_instance=context)
