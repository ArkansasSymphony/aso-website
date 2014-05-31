from arkansassymphony.donation.models import *
from django.contrib import admin

class DonationAdmin(admin.ModelAdmin):
	list_display = ('name', 'donation', 'anonymous', 'email', 'notes')

admin.site.register(Donation, DonationAdmin)
