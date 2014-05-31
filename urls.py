from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views


#Enable the admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/musicians/report/$', 'arkansassymphony.musicians.admin_views.report'),
	(r'^admin/checkin/patron/(?P<id>[\d]+)/go', 'arkansassymphony.checkin.admin_views.go'),
	(r'^admin/', include(admin.site.urls)),
	(r'^about/jobs/', include('arkansassymphony.jobs.urls')),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
)

urlpatterns += patterns('arkansassymphony.views',
	(r'^$', 'mainPage'),
	(r'^(?i)pick3/$', 'pick2'),
	(r'^(?i)guild/$', 'pick2guild'),
	(r'^longterm/$', 'loyalty'),
	(r'^thanks/$', direct_to_template, {'template': 'thanks.html'}), 
	(r'^(?i)season/$', 'season'),
	(r'^summer-strings$', direct_to_template,  {'template': 'summer_strings.html'}),
	(r'^youth-rock$', direct_to_template,  {'template': 'youthrock.html'}),
	(r'^renovation$', direct_to_template, {'template': 'concerts/renovation_faq.html'}),
	(r'^street-party$', direct_to_template, {'template': 'bbj_party.html'}),
	(r'^ccg-composer-contest$', direct_to_template, {'template': 'ccg_contest.html'}),
)

urlpatterns += patterns('arkansassymphony.registration.views',
    url(r'^asyo/register/', 'register_user'),
    url(r'^asyo/members/', 'members_area'),
    url(r'^asyo/admin/', 'admin_area'),
    url(r'^asyo/student/','register_student'),
    url(r'^asyo/update/p/(?P<parent>\d+)/$', 'update_parent'),
    url(r'^asyo/update/s/(?P<student>\d+)/$', 'update_student'),
    url(r'^asyo/delete/s/(?P<student>\d+)/$', 'delete_student'),
    url(r'^asyo/application/(?P<student>\d+)/$', 'student_application'),
    url(r'^asyo/update/app/(?P<id>\d+)/$', 'update_app'),
    url(r'^asyo/delete/app/(?P<id>\d+)/$', 'delete_app'),
    url(r'^asyo/logout/', 'logout_user'),
    url(r'^asyo/appadminjson/$', 'app_admin_json'),
    url(r'^asyo/appjson/$', 'app_json'),
    url(r'^asyo/studentjson/$', 'student_json'),
    url(r'^asyo/parentjson/$', 'parent_json'),
)

urlpatterns += patterns('arkansassymphony.designerhouse.views',
	url(r'^designer-house/$', 'designer_main', name='designer_main'),
	url(r'^designer-house/about/$', 'about_view', name='about_view'),
	url(r'^designer-house/sponsors/$', 'sponsor_view', name='sponsor_view'),
	url(r'^designer-house/designers/$', 'designer_view', name='designer_view'),
	url(r'^designer-house/tickets/$', 'tickets_view', name='tickets_view'),
	url(r'^designer-house/(?P<party_url>[\w-]+)/$', 'party_view', name='party_view'),
)

urlpatterns += patterns('arkansassymphony.checkin.form_views',
	url(r'^checkin$', 'patron_formview', name="patron_formview"),
	url(r'^charge/$', 'charge_formview', name="charge_formview"),
)

urlpatterns += patterns('arkansassymphony.donation.form_views',
	url(r'^donate$', 'donation_formview', name='donation_formview'),
	url(r'^donate/$', 'donation_formview', name='donation_formview'),
	url(r'^support$', 'donation_formview', name='donation_formview'),
	url(r'^support/$', 'donation_formview', name='donation_formview'),
)

#rsvp form urls
urlpatterns += patterns('arkansassymphony.rsvp.form_views',
	url(r'^rsvp$', 'RSVP_formview', name='RSVP_formview'),
	url(r'^rsvp/$', 'RSVP_formview', name='RSVP_formview'),
)

#rsvp data urls
urlpatterns += patterns('arkansassymphony.rsvp.views',
	url(r'^rsvp/rsvp-info$', 'rsvp_info', name='rsvp_info'),
	url(r'^rsvp/rsvp-info/$', 'rsvp_info', name='rsvp_info'),
)

urlpatterns += patterns('arkansassymphony.galleries.views',	
	url(r'^connect/media$', direct_to_template, {'template': 'gallery/media-page.html'}),
	url(r'^connect/media/(?P<media_type>[\w-]+)$', 'galleries_view', name='galleries_views'),
	url(r'^connect/media/galleries/(?P<gallery_url>[\w-]+)', 'photos_view', name='photos_view'),
	url(r'^connect/media/galleries/(?P<gallery_url>[\w-]+)/(?P<photo_name>\file)$', 'single_photo', name='single_photo'),
)


urlpatterns += patterns('',
	(r'^concerts/benefits/', direct_to_template, {'template': 'concerts/benefits.html'}),
	(r'^concerts/groups/', direct_to_template, {'template': 'concerts/groups.html'}),
	(r'^concerts/pricingseating/', direct_to_template, {'template': 'concerts/pricingseating.html'}),
	(r'^concerts/donate/', direct_to_template, {'template': 'concerts/donate.html'}),
	(r'^concerts/boxoffice/', direct_to_template, {'template': 'concerts/boxoffice.html'}),
	
	
	(r'^themusic/musicdirector/', direct_to_template, {'template': 'themusic/musicdirector.html'}),
	(r'^themusic/associate/', direct_to_template, {'template': 'themusic/associate.html'}),
	(r'^themusic/talks/', direct_to_template, {'template': 'themusic/talks.html'}),
	(r'^themusic/$', direct_to_template, {'template': 'themusic/themusic.html'}),
	
	
	(r'^support/opusball/', direct_to_template, {'template': 'support/opusball.html'}),
	(r'^support/corporate/', direct_to_template, {'template': 'support/corporate.html'}),
	(r'^support/foundation/', direct_to_template, {'template': 'support/foundation.html'}),
	(r'^support/volunteer/', direct_to_template, {'template': 'support/volunteer.html'}),
	(r'^support/benefits/', direct_to_template, {'template': 'support/benefits.html'}),
	#(r'^support/$', direct_to_template, {'template': 'support/support.html'}),
	#(r'^support/designerhouse/$', direct_to_template, {'template': 'support/designerhouse.html'}),	


	(r'^education/youngartist/$', direct_to_template, {'template': 'education/youngartist.html'}),	
	(r'^education/youthorchestras/johnjarboe/', direct_to_template, {'template': 'education/johnjarboe.html'}),
	(r'^education/youthorchestras/caseybuck/', direct_to_template, {'template': 'education/caseybuck.html'}),
	(r'^education/youthorchestras/jameshatch/', direct_to_template, {'template': 'education/jameshatch.html'}),
	(r'^education/youthorchestras/tommcdonald', direct_to_template, {'template': 'education/tommcdonald.html'}),
	(r'^education/youthorchestras/$', direct_to_template, {'template': 'education/youthorchestras.html'}),
	(r'^education/auditions/$', direct_to_template, {'template': 'education/auditioninfo.html'}),
	(r'^education/artspartners/', direct_to_template, {'template': 'education/artspartners.html'}),
	(r'^education/quartet-visits/', direct_to_template, {'template': 'education/artspartners.html'}),
	(r'^education/orchestraandyou/', direct_to_template, {'template': 'education/orchestraandyou.html'}),
	(r'^education/chilrensconcerts/', direct_to_template, {'template': 'education/childrensconcertshtml'}),
	(r'^education/childrensconcerts/', direct_to_template, {'template': 'education/childrensconcerts.html'}),
	(r'^education/$', direct_to_template, {'template': 'education/programs.html'}),
	(r'^education/stringdrive/', direct_to_template, {'template': 'education/stringdrive.html'}),
		

	(r'^(?i)offers/combo/$', direct_to_template, {'template': 'concerts/mw_combo.html'}),	
	(r'^(?i)offers/mw1/$', direct_to_template, {'template': 'concerts/mw1_offer.html'}),
	(r'^(?i)offers/ch1/$', direct_to_template, {'template': 'concerts/ch1_offer.html'}),
	(r'^(?i)offers/p1/$', direct_to_template, {'template': 'concerts/pops1_offer.html'}),
	(r'^(?i)offers/mw2/$', direct_to_template, {'template': 'concerts/mw2_offer.html'}),
	(r'^(?i)offers/ch2/$', direct_to_template, {'template': 'concerts/ch2_offer.html'}),
	(r'^(?i)offers/mw3/$', direct_to_template, {'template': 'concerts/mw3_offer.html'}), 
	(r'^(?i)offers/inc1/$', direct_to_template, {'template': 'concerts/inc1_offer.html'}), 
)
#teacher urls
urlpatterns += patterns('arkansassymphony.teachers.views',
	url(r'^education/teachers/$', 'teacher_view', name="teacher_view"),
)

#venue urls
urlpatterns += patterns('arkansassymphony.venue.views',
	url(r'^venue/$', 'venue_landing', name="venue_landing"),
	url(r'^visit/$', 'venue_landing', name="venue_landing"),
	url(r'^venue/(?P<venue_url>[\w-]+)/', 'venue_view', name="venue_view"),
)
	
#Musicians' portal urls
urlpatterns += patterns('arkansassymphony.musicians.views',
	url(r'^musicians/$', 'musician_portal', name="musician_portal"),
	url(r'^musicians/information/$', 'information', name="information"),
	url(r'^musicians/concert-info/$', 'concert_info', name="concert_info"),
	url(r'^musicians/concert-info/(?P<concert_name>[\w-]+)/', 'concert_view', name="concert_view"),
	url(r'^musicians/info/', 'info', name="info"),
	url(r'^musicians/wage-chart/', 'wage_info', name="wage_info"),
	url(r'^musicians/faq/', 'faq', name="faq"),
	url(r'^musicians/MA/ma-contents/$', 'ma_contents', name="ma_contents"),
	url(r'^musicians/MA/(?P<part>\d+)/', 'ma', name="ma"),
	url(r'^musicians/calendars/$', 'calendars', name="calendars"),
	url(r'^musicians/calendars/reservations/', 'reservations', name="reservations"),
	url(r'^musicians/contact/$', 'contact', name="contact"),
	url(r'^musicians/staff-contact/$', 'staff_contact', name="staff_contact"),
	url(r'^musicians/forms/$', 'forms', name="forms"),
	url(r'^musicians/hr/$', 'hr', name="hr"),
	url(r'^musicians/musician-forms/$', 'musician_forms', name="musician_forms"),
	url(r'^musicians/venues/$', 'venues', name="venues"),
	url(r'^musicians/venues/(?P<venue_url>[\w-]+)/', 'venue_detail', name="venue_detail"),
	url(r'^musicians/bus-info/$', 'bus_info', name="bus_info"),
)

#musician site form urls
urlpatterns += patterns('arkansassymphony.musicians.form_views',
	#"submitted" redirect
	url(r'^musicians/forms/contact/thanks/$', 'thanks', name="thanks"),
	#actual forms here
	url(r'^musicians/forms/byrne-request/$', 'byrne_form', name="byrne_form"),
	url(r'^musicians/forms/van-request/$', 'van_form', name="van_form"),
	url(r'^musicians/forms/service-claim/$', 'service_claim', name="service_claim"),
	url(r'^musicians/forms/comp-tickets/$', 'comp_request', name="comp_request"),
	url(r'^musicians/forms/hotel-request/$', 'hotel_request', name="hotel_request"),
	url(r'^musicians/bus-info/(?P<show_url>[\w-]+)/', 'bus_form', name="bus_form"),
)

urlpatterns += patterns('arkansassymphony.staff_board.views',
	url(r'^about$', 'about', name="about"),
	url(r'^connect/contactus/', 'contactus', name="contactus"),
)
urlpatterns += patterns('arkansassymphony.concerts.views',
	(r'^concerts/subscriptions/', 'subscriptionPage'),

	(r'^(?i)irresistible/', 'subscriptionPage'),
	
	(r'^concerts/masterworks/(?P<display>\w+)/(?P<season>[\d-]+)/$', 'mwPage'),
	(r'^concerts/pops/(?P<display>\w+)/(?P<season>[\d-]+)/$', 'popsPage'),
	(r'^concerts/chamber/(?P<display>\w+)/(?P<season>[\d-]+)/$', 'chamberPage'),
	(r'^concerts/neighborhood/(?P<display>\w+)/(?P<season>[\d-]+)/$', 'neighborhoodPage'),
	(r'^concerts/all/(?P<display>\w+)/(?P<season>[\d-]+)/$', 'concertsPage'),
	
	(r'^concerts/(?P<urlName>[\w-]+)/', 'showDetail'),
	
	(r'^artists/(?P<urlName>[\w-]+)/(?P<showUrlName>[\w-]+)/', 'artistPage'),

	(r'^themusic/notes/(?P<urlName>[\w-]+)/(?P<showUrlName>[\w-]+)/', 'noteDetail'),
	(r'^themusic/notes/(?P<sortBy>[\w-]+)/', 'notePage'),
	
	(r'^(?i)education/freekids/$', 'freeKids'),
	(r'^(?i)freekids/$', 'freeKids'),
	
)


urlpatterns += patterns('arkansassymphony.people.views',
	(r'^themusic/orchestra/(?P<playerId>\w+)/', 'orchestraBio'),
	(r'^themusic/orchestra/', 'orchestraPage'),
)


urlpatterns += patterns('arkansassymphony.comments.views',
	(r'^welcome/comment/', 'welcomeForm'),
	(r'^welcome/$', 'welcomePage'),
        (r'^connect/event/(?P<showUrl>\w+)/viewcomments/', 'eventViewComments'),

)

urlpatterns += patterns('arkansassymphony.youthcalendar.views',
        (r'^education/youthorchestras/schedule/(?P<group>\w+)/', 'schedule'),
)

