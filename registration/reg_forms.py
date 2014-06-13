from django.forms import ModelForm
from django import forms
from models import *
from django.forms.extras.widgets import SelectDateWidget
from asyo_enums import *

# here are our forms for asyo
# inheriting from ModelForm
# git push clone test

class PrimaryGuardianForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = PrimaryGuardian
		exclude = ["date_created","last_updated"]

class StudentForm(ModelForm):
	#date_of_birth = forms.DateField(widget=SelectDateWidget(years=YEARS))
	class Meta:
		model = Student
		exclude = ["status","current_grade","date_created","last_updated","parent_id","start_date"]


class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		exclude = ["app_student_id","app_parent_id","application_date", "read_agree_terms"]

class ApplicationAdminForm(ModelForm):
	class Meta:
		model = ApplicationAdmin
