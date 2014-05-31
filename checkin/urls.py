from django.conf.urls.defaults import *
from arkansassymphony.checkin import views
 
urlpatterns = patterns('',
    url(r'^charge/$', views.charge, name="charge"),
)