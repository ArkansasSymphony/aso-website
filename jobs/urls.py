from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views


urlpatterns = patterns('arkansassymphony.jobs.views',
	url(r'^$', 'jobsMain', name='jobsMain'),	
	(r'^(?P<jobTitle>[\w-]+)/$', 'jobDetail'),
)


