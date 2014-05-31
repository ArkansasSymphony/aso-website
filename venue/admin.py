from arkansassymphony.venue.models import *
from django.contrib import admin

class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'venue_type', 'status')

admin.site.register(Venue, VenueAdmin)
