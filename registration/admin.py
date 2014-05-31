from django.contrib import admin
from models import *

# Register your models here.
class PrimaryGuardianAdmin(admin.ModelAdmin):
	list_display = ("last_name","first_name", "email")
	search_fields = ["last_name", "first_name"]

class StudentAdmin(admin.ModelAdmin):
	list_display = ("last_name",
		"first_name",
		"email",
		"current_grade",
		"instrument",
		"status")
	search_fields = ["last_name","first_name","parent_id"]
	list_filter = ("status",)

class ApplicationA(admin.ModelAdmin):
	list_display = ("app_student_id",
		"applying_for",
		"age_as_of_sept",
		"grade_as_of_sept",
		"returning_student",
		"all_state",
		"all_region")
	search_fields = ["app_student_id","grade_as_of_sept","returning_student"]
	list_filter = ("grade_as_of_sept","applying_for",)

class ApplicationAdminAdmin(admin.ModelAdmin):
	list_display = ("sua_app_id",
		"approve_for_group",
		"paid",
		"paid_amount",
		"paid_notes",
		"date_paid_in_full",
		"approved_by","date_approved")
	search_fields = ["sua_app_id"]
	list_filter = ("paid",)


admin.site.register(PrimaryGuardian,PrimaryGuardianAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Application,ApplicationA)
admin.site.register(ApplicationAdmin, ApplicationAdminAdmin)
