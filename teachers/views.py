from django.shortcuts import render_to_response
from arkansassymphony.teachers.models import *
from django.template import RequestContext


def teacher_view(request):
	teachers = Teacher.objects.all()
	violin_group = Teacher.objects.filter(instrument="violin").order_by('order')
	viola_group = Teacher.objects.filter(instrument="viola").order_by('order')
	cello_group = Teacher.objects.filter(instrument="cello").order_by('order')
	bass_group = Teacher.objects.filter(instrument="bass").order_by('order')
	flute_group = Teacher.objects.filter(instrument="flute").order_by('order')
	oboe_group = Teacher.objects.filter(instrument="oboe").order_by('order')
	clarinet_group = Teacher.objects.filter(instrument="clarinet").order_by('order')
	english_horn_group = Teacher.objects.filter(instrument="english horn").order_by('order')
	bassoon_group = Teacher.objects.filter(instrument="bassoon").order_by('order')
	saxophone_group = Teacher.objects.filter(instrument="saxophone").order_by('order')
	horn_group = Teacher.objects.filter(instrument="horn").order_by('order')
	trumpet_group = Teacher.objects.filter(instrument="trumpet").order_by('order')
	tuba_group = Teacher.objects.filter(instrument="tuba").order_by('order')
	trombone_group = Teacher.objects.filter(instrument="trombone").order_by('order')
	percussion_group = Teacher.objects.filter(instrument="percussion").order_by('order')
	harp_group = Teacher.objects.filter(instrument="harp").order_by('order')
	piano_group = Teacher.objects.filter(instrument="piano").order_by('order')

	strings = ['violin', 'viola', 'cello', 'bass']
	woodwinds = ['flute', 'oboe', 'clarinet', 'english horn', 'bassoon', 'saxophone']
	brass = ['horn', 'trumpet','trombone', 'tuba']
	percussion = ['percussion']
	harp = ['harp']
	piano = ['piano']
	
	string_teachers = ""
	woodwind_teachers = ""
	brass_teachers = ""
	percussion_teachers = ""
	harp_teachers = ""
	piano_teachers = ""


	for teacher in teachers:
		if teacher.instrument in strings:
			string_teachers = "yes"
		elif teacher.instrument in woodwinds:
			woodwind_teachers = "yes"
		elif teacher.instrument in brass:
			brass_teachers = "yes"
		elif teacher.instrument in percussion:
			percussion_teachers = "yes"
		elif teacher.instrument in harp:
			harp_teachers = "yes"
		elif teacher.instrument in piano:
			piano_teachers = "yes"

	return render_to_response('education/teachers.html', {'violin_group': violin_group, 'viola_group': viola_group, 'cello_group': cello_group, 'bass_group': bass_group, 'flute_group': flute_group, 'oboe_group': oboe_group, 'clarinet_group': clarinet_group, 'english_horn_group': english_horn_group, 'bassoon_group': bassoon_group, 'saxophone_group': saxophone_group, 'horn_group': horn_group, 'trumpet_group': trumpet_group, 'trombone_group': trombone_group, 'tuba_group': tuba_group, 'percussion_group': percussion_group, 'harp_group': harp_group, 'piano_group': piano_group, 'string_teachers': string_teachers, 'woodwind_teachers': woodwind_teachers, 'brass_teachers': brass_teachers, 'percussion_teachers': percussion_teachers, 'harp_teachers': harp_teachers, 'piano_teachers': piano_teachers,}, context_instance=RequestContext(request))
