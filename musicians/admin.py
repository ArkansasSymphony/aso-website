from arkansassymphony.musicians.models import *
from django.contrib import admin

class WageAdmin(admin.ModelAdmin):
    list_display = ('fiscal_year', 'principal_performance', 'section_performance')

class CompAdmin(admin.ModelAdmin):
	list_display = ('musician_name', 'show', 'day', 'quantity', 'delivery', 'notes')
	
class ClaimAdmin(admin.ModelAdmin):
	list_display = ('name', 'form_type', 'service', 'mileage_claim', 'diem_claim', 'cartage_claim', 'doubling_claim', 'total_claim')

class StopInline(admin.StackedInline):
	model = BusStop
	extra = 1

class ScheduleInline(admin.StackedInline):
	model = Schedule
	extra = 1
	
class ConcertAdmin(admin.ModelAdmin):
	list_display = ('name', 'end_date', 'type', 'venue', 'comps_available', 'bus_service')
	prepopulated_fields = {"url_name": ("name",)}
	inlines = [StopInline, ScheduleInline]
	
class VenueAdmin(admin.ModelAdmin):
	prepopulated_fields = {"url_name": ("name",)}

class BusFormAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'riding', 'boarding', 'meal')

class HotelFormAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'check_in', 'check_out', 'room_type', 'roommate_request')

class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'service_type', 'service_note')
	ordering = ['date']

admin.site.register(HRDocument)
admin.site.register(Service, ServiceAdmin)
admin.site.register(HotelForm, HotelFormAdmin)
admin.site.register(BusForm, BusFormAdmin)	
admin.site.register(WageChart, WageAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(ConcertDocument)
admin.site.register(ProgramItem)
admin.site.register(CompTicket, CompAdmin)
admin.site.register(AdminClaimForm, ClaimAdmin)
admin.site.register(Venue, VenueAdmin)
