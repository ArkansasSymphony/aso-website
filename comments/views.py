import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from arkansassymphony.comments.models import Comment
from arkansassymphony.comments.forms import CommentForm
from arkansassymphony.concerts.models import Show

def welcomePage(request):
	commentList = Comment.objects.filter(show__isnull=True).order_by('-posted')
		
	context = RequestContext(request)
	return render_to_response('themusic/welcome.html', {'commentList': commentList}, context_instance=context)


def welcomeForm(request):
	captcha_error = ""

	if request.method == 'POST':
        	form = CommentForm(request.POST)

		captcha_response = captcha.submit(request.POST.get("recaptcha_challenge_field", None), request.POST.get("recaptcha_response_field", None), "6LeXfr0SAAAAAEAzaSWLoLBqrNHU0so-H7dgQhoz", 
request.META.get("REMOTE_ADDR", None),)

		if not captcha_response.is_valid:
			captcha_error = "&error=%s" % captcha_response.error_code

		elif form.is_valid():
			theComment = Comment()
			theComment.name = form.cleaned_data['name']
			theComment.message = form.cleaned_data['message']
			theComment.posted = datetime.datetime.now()
			theComment.save()
			return HttpResponseRedirect('/welcome/')
	else:
	        form = CommentForm()

	return render_to_response('themusic/welcomeform.html', {'form': form, 'captcha_error': captcha_error})



def eventViewComments(request, showUrl):
        commentList = Comment.objects.filter(show__url_name = showUrl).order_by('-posted')
	showList = Show.objects.filter(url_name = showUrl)

        context = RequestContext(request)
        return render_to_response('connect/event_comments.html', {'commentList': commentList, 'show': showList[0]}, context_instance=context)

"""
def eventComment(request, showUrl):
        captcha_error = ""

	showList = Show.objects.filter(url_name = showUrl)


        if request.method == 'POST':
                form = CommentForm(request.POST)

                captcha_response = captcha.submit(request.POST.get("recaptcha_challenge_field", None), request.POST.get("recaptcha_response_field", None), "6LeXfr0SAAAAAEAzaSWLoLBqrNHU0so-H7dgQhoz",
request.META.get("REMOTE_ADDR", None),)

                if not captcha_response.is_valid:
                        captcha_error = "&error=%s" % captcha_response.error_code

                elif form.is_valid():
                        theComment = Comment()
                        theComment.name = form.cleaned_data['name']
                        theComment.message = form.cleaned_data['message']
                        theComment.posted = datetime.datetime.now()
			
			theComment.show = showList[0]
                        theComment.save()
                        return HttpResponseRedirect('/connect/event/%(showUrl)s/viewcomments/' % {'showUrl': showUrl})
        else:
                form = CommentForm()

	return render_to_response('connect/event_commentform.html', {'form': form, 'captcha_error': captcha_error, 'show': showList[0]})
"""
