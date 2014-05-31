from arkansassymphony.designerhouse.models import *
from django.contrib import admin

class PartyAdmin(admin.ModelAdmin):
	prepopulated_fields = {"url_name": ("name",)}

admin.site.register(Party, PartyAdmin)
admin.site.register(Sponsor)
admin.site.register(Designer)
