from arkansassymphony.youthcalendar.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
	list_filter = ['date']
	search_fields = ['name']
	list_display = ('name', 'group', 'date')

admin.site.register(Event,EventAdmin)


