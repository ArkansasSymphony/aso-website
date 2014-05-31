from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from reg_forms import *
from models import *
import datetime,json
from django.core import serializers

# our views for asyo registration app

###################################
## register views 
###################################
def register_user(request):
	if request.method == 'POST':
		form = PrimaryGuardianForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			obj = form.save(commit=False)
			user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
			form.save()
			user.save()
			user_login = authenticate(username=cd['username'],password=cd['password'])
			if user_login is not None:
				if user_login.is_active:
					login(request,user_login)
					return redirect('/asyo/members/')
	else:
		form = PrimaryGuardianForm()
	return render(request,'asyo/index.html',{'reg_form': form, })

@login_required(login_url='/accounts/login/')
def register_student(request):
	if request.method == 'POST':
		student_form = StudentForm(request.POST)
		if student_form.is_valid():
			cd = student_form.cleaned_data
			obj = student_form.save(commit=False)
			parent = PrimaryGuardian.objects.filter(username=request.user)
			obj.parent_id = parent[0]
			student_form.save()
			return redirect('/asyo/members/')
	else:
		student_form = StudentForm()
	app_parent = PrimaryGuardian.objects.get(username=request.user)
	return render(request,'asyo/student_register.html',{'app_parent':app_parent, 'reg_form':student_form,})

@login_required(login_url='/accounts/login/')
def student_application(request, student):
	student = Student.objects.filter(pk=student)[0]
	message = ''
	if request.method == 'POST':
		app_form = ApplicationForm(request.POST)
		if app_form.is_valid():
			cd = app_form.cleaned_data
			obj = app_form.save(commit=False)
			obj.app_student_id = student
			obj.app_parent_id = PrimaryGuardian.objects.filter(username=request.user.username)[0]
			obj.application_date = datetime.datetime.now()
			app_form.save()
			app = Application.objects.filter(app_student_id=student)[0]
			ApplicationAdmin(sua_app_id=app).save()
			return redirect('/asyo/members/')
	else:
		if len(Application.objects.filter(app_student_id=student)) == 0:
			app_form = ApplicationForm()
		else:
			app_form = ""
			message = "%s already has applied" % student
		#vars['reg_form'] = app_form

	app_parent = PrimaryGuardian.objects.get(username=request.user)

	vars = {
		'app_parent' : app_parent,
		'student' : student,
		'reg_form' : app_form,
		'message' : message,
	}
	return render(request,'asyo/apply.html',vars)

##################################################
## Members only views and actions
##################################################

@login_required(login_url='/accounts/login/')
def members_area(request):
	vars = {}

	vars['user'] = PrimaryGuardian.objects.get(username=request.user)
	p = PrimaryGuardian.objects.filter(username=request.user.username)[0]

	vars['students'] = Student.objects.filter(parent_id = p)
	vars['applications'] = Application.objects.filter(app_parent_id=p)

	if len(vars['students']) == 0:
		vars['student_present'] = 'False'
	else:
		vars['student_present'] = 'True'

	if len(vars['applications']) == 0:
		vars['application_present'] = 'False'
	else:
		vars['application_present'] = 'True'

	return render(request,'asyo/members_area.html',vars)


@login_required(login_url='/accounts/login/')
def delete_student(request,student):
	s = Student.objects.get(pk=student)
	s.delete()
	return redirect('/asyo/members/')

@login_required(login_url='/accounts/login/')
def delete_app(request,id):
	s = Application.objects.get(pk=id)
	s.delete()
	return redirect('/asyo/members/')

@login_required(login_url='/accounts/login/')
def update_app(request,id):
	message = ''
	a = get_object_or_404(Application,pk=id)
	student = a.app_student_id
	app_parent = PrimaryGuardian.objects.get(username=request.user)
	if request.method == 'POST':
		app_form = ApplicationForm(request.POST,instance=a)
		if app_form.is_valid():
			ua = app_form.save(commit=False)
			ua.save()
			return redirect('/asyo/members/')
	else:
		form = ApplicationForm(instance=a)
	return render(request,'asyo/apply.html',{'reg_form':form,"message":message, 'student': student, 'app_parent': app_parent})

@login_required(login_url='/accounts/login/')
def update_student(request,student):
	message = ''
	updating = ''
	app = get_object_or_404(Student,pk=student)
	app_parent = PrimaryGuardian.objects.get(username=request.user)
	if request.method == 'POST':
		#testing - changed s_app to form and may need to change back from next line through end of if statement
		form = StudentForm(request.POST,instance=app)
		if form.is_valid():
			usa = form.save(commit=False)
			usa.save()
			return redirect('/asyo/members/')
	else:
		form = StudentForm(instance=app)
	return render(request,'asyo/student_register.html',{'reg_form':form, 'app_parent': app_parent, 'updating': updating})

@login_required(login_url='/accounts/login/')
def update_parent(request,parent):
	message = ''
	updating = ''
	app = get_object_or_404(PrimaryGuardian,pk=parent)
	if request.method == 'POST':
		form =PrimaryGuardianForm(request.POST,instance=app)
		if form.is_valid():
			usa = form.save(commit=False)
			usa.save()
			return redirect('/asyo/members/')
	else:
		form = PrimaryGuardianForm(instance=app)
	return render(request,'asyo/index.html',{'reg_form':form,'updating': updating})

##############################
## Admin Views
##############################

## using the admin interface
@staff_member_required
@login_required(login_url='/accounts/login/')
def admin_area(request):
	vars = {}
	pg = Application.objects.all()
	aa = ApplicationAdmin.objects.all()
	parents = PrimaryGuardian.objects.all()
	students = Student.objects.all()
	vars['applications'] = pg
	vars['current_user'] = request.user
	vars['app_admins'] = aa
	vars['parents'] = parents
	vars['students'] = students
	return render(request,'asyo/admin.html',vars)


#####################################
## application wide views
#####################################
def logout_user(request):
	logout(request)
	return redirect('/asyo/members/')

#####################################
## data sources for tables 
#####################################

@staff_member_required
@login_required(login_url='/accounts/login/')
def app_admin_json(request):
	s = ApplicationAdmin.objects.all()
	obj = [{
			"0":a.sua_app_id.app_student_id.first_name+" "+a.sua_app_id.app_student_id.last_name,
			"1":a.approve_for_group,
			"2":str(a.date_approved),
			"3":a.approved_by, 
			"4":a.paid,
			"5":a.paid_amount,
			"6":a.paid_notes,
			"7":str(a.date_paid_in_full)} for a in s]
	response = {"aaData": obj}
	return HttpResponse(json.dumps(response),content_type='application/json')

@staff_member_required
@login_required(login_url='/accounts/login/')
def student_json(request):
	s = Student.objects.all()
	obj = [{
			"0":a.first_name+" "+a.last_name,
			"1":a.cell_phone,
			"2":a.email, 
			"3":a.current_grade,
			"4":a.instrument,
			"5":a.status} for a in s]
	response = {"aaData": obj}
	return HttpResponse(json.dumps(response),content_type='application/json')

@staff_member_required
@login_required(login_url='/accounts/login/')
def parent_json(request):
	s = PrimaryGuardian.objects.all()
	obj = [{
			"0":a.first_name+" "+a.last_name,
			"1":a.address,
			"2":a.city, 
			"3":a.state,
			"4":a.zipcode,
			"5":a.cell_phone,
			"6":a.email,
			"7":a.preferred_com_method} for a in s]
	response = {"aaData": obj}
	return HttpResponse(json.dumps(response),content_type='application/json')

@staff_member_required
@login_required(login_url='/accounts/login/')
def app_json(request):
	s = Application.objects.all()
	obj = [{
			"0":a.app_student_id.first_name+" "+a.app_student_id.last_name,
			"1":a.applying_for,
			"2":a.application_year, 
			"3":str(a.application_date),
			"4":a.age_as_of_sept,
			"5":a.current_grade} for a in s]
	response = {"aaData": obj}
	return HttpResponse(json.dumps(response),content_type='application/json')
