import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from arkansassymphony.youthcalendar.models import Event


def schedule(request, group):

	eventList = Event.objects.filter(date__gte = datetime.date.today()).filter(group = '%s' % group).order_by('date') | Event.objects.filter(date__gte = datetime.date.today()).filter(group = 'all').order_by('date')



        context = RequestContext(request)
        return render_to_response('education/schedule.html', {'eventList': eventList, 'group': group}, context_instance=context)



