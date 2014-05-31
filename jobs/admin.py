from arkansassymphony.jobs.models import Job
from django.contrib import admin

class JobAdmin(admin.ModelAdmin):
        prepopulated_fields = {"url_name": ("title",)}

admin.site.register(Job, JobAdmin)


