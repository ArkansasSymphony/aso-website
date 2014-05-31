from django.shortcuts import render_to_response
from django.template import RequestContext
from arkansassymphony.people.models import Artist, Instrument, Player


def orchestraBio(request, playerId):
	playerList = Player.objects.filter(id = '%s' % playerId)
	thePlayer = playerList[0]

	context = RequestContext(request)
        return render_to_response('themusic/orchestra_bio.html', {'player': thePlayer}, context_instance=context)



def orchestraPage(request):
	playerList = Player.objects.all().order_by('instrument__list_order').order_by('section_order')

	instrumentList = Instrument.objects.all().order_by('list_order')
	
	totalCount = 0
	
	for instrument in instrumentList:
		totalCount = totalCount + 1
	
	for player in playerList:
		totalCount = totalCount + 1
	
	count = 0
	
	col1List = []
	col2List = []

	col2 = False
	
	for instrument in instrumentList:
		
		if count > (totalCount / 2):
			col2 = True


		if col2 == True:
			col2List.append("pre_inst")
			col2List.append(instrument.name)
			col2List.append("post_inst")
			count = count + 1
		else:
			col1List.append("pre_inst")
			col1List.append(instrument.name)
			col1List.append("post_inst")
			count = count + 1
		
		for player in playerList:
			if player.instrument == instrument:
				if player.bio:
					entry = "<a href='/themusic/orchestra/%(id)d/' class='medBlue'>%(name)s</a>" % {'id': player.id, 'name': player.name}
				else:
					entry = player.name

				if player.chair_name:
					entry = entry + "<br><font size='1'><i>" + player.chair_name + "</i></font>"

				if col2 == True:
					col2List.append(entry)
					count = count + 1

				else:
					col1List.append(entry)
					count = count + 1

				
		
		if col2 == True:
			col2List.append("pre_inst")
			col2List.append("")
			col2List.append("post_inst")
		else:
			col1List.append("pre_inst")
			col1List.append("")
			col1List.append("post_inst")
			
		
	context = RequestContext(request)
	return render_to_response('themusic/orchestra.html', {'col1List': col1List, 'col2List': col2List}, context_instance=context)
	
