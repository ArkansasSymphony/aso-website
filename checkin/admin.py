from arkansassymphony.checkin.models import *
from django.contrib import admin

class PatronAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'organization', 'cc_number', 'bid_number', 'checked_in', 'dining_assignment', 'notes')
	search_fields = ('last_name', 'organization', 'bid_number')

class ChargeAdmin(admin.ModelAdmin):
	list_display = ('description', 'item_number', 'price', 'customer', 'payment_method')

admin.site.register(Patron, PatronAdmin)
admin.site.register(Charge, ChargeAdmin)
