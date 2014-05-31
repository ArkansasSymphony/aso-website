from arkansassymphony.rsvp.models import *
from django.contrib import admin

class RSVPAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'quantity', 'email', 'notes')

admin.site.register(RSVP, RSVPAdmin)
