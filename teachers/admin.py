from arkansassymphony.teachers.models import *
from django.contrib import admin

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'instrument', 'notes')

admin.site.register(Teacher, TeacherAdmin)
