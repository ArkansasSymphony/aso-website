from django.db import models
from asyo_enums import *

# Form models for asyo 
class PrimaryGuardian(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    cell_phone = models.CharField(max_length=15, blank=True)
    home_phone = models.CharField(max_length=15, blank=True)
    other_phone = models.CharField(max_length=15, null=True,blank=True)
    primary_phone = models.CharField(max_length=10, choices=PRIMARY_NUMBER)
    email = models.EmailField(max_length=100, unique=True)
    preferred_com_method = models.CharField(max_length=10, choices=PREFERRED_COM_METHOD)
    employer = models.CharField(max_length=100, null=True,blank=True)
    spouse_last_name = models.CharField(max_length=30, null=True,blank=True)
    spouse_first_name = models.CharField(max_length=30, null=True,blank=True)
    spouse_cell_phone = models.CharField(max_length=15, null=True,blank=True)
    spouse_home_phone = models.CharField(max_length=15, null=True,blank=True)
    spouse_other_phone = models.CharField(max_length=15, null=True,blank=True)
    spouse_primary_number = models.CharField(max_length=15, null=True,blank=True)
    spouse_email = models.EmailField(max_length=100, null=True,blank=True)
    spouse_address = models.CharField(max_length=50, null=True,blank=True)
    spouse_city = models.CharField(max_length=50, null=True,blank=True)
    spouse_state = models.CharField(max_length=2, null=True,blank=True)
    spouse_zipcode = models.CharField(max_length=5, null=True,blank=True)
    spouse_employer = models.CharField(max_length=100, null=True,blank=True)
    notes = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def primary_contact_info(self):
    	if self.preferred_com_method == 'Email':
    		return self.email
    	else:
    		return self.primary_phone
    
    
class Student(models.Model):
    parent_id = models.ForeignKey(PrimaryGuardian)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    cell_phone = models.CharField(max_length=15,null=True,blank=True)
    home_phone = models.CharField(max_length=15,null=True,blank=True)
    other_phone = models.CharField(max_length=15,null=True,blank=True)
    primary_phone = models.CharField(max_length=15, choices=PRIMARY_NUMBER)
    email = models.EmailField(max_length=100)
    #date_of_birth = models.DateField()
    current_grade = models.CharField(max_length=2,choices=GRADE_LEVEL, null=True,blank=True)
    graduating_year = models.CharField(max_length=20, choices=GRAD_YEAR, null=True, blank = False)
    instrument = models.CharField(max_length=20,choices=INSTRUMENTS, null=True,blank=True)
    start_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    


class Application(models.Model):
    app_parent_id = models.ForeignKey(PrimaryGuardian)
    app_student_id = models.OneToOneField(Student)
    applying_for = models.CharField(max_length=255, choices=ORCHESTRA_TYPE)
    application_year = models.PositiveSmallIntegerField(max_length=4, choices=ENUM_YEARS)
    application_date = models.DateField()
    age_as_of_sept = models.PositiveSmallIntegerField(max_length=2,choices=AGE)
    grade_as_of_sept = models.CharField(max_length=2,choices=GRADE_LEVEL)
    #current_grade = models.CharField(max_length=2,choices=GRADE_LEVEL)
    returning_student = models.CharField(max_length=1, choices=YES_NO)
    all_state = models.CharField(max_length=1, choices=YES_NO, null=True,blank=True)
    all_region = models.CharField(max_length=1, choices=YES_NO, null=True,blank=True)
    local_paper = models.CharField(max_length=100, null=True,blank=False)
    local_paper_address = models.CharField(max_length=100, null=True,blank=False)
    school = models.CharField(max_length=100, blank = False)
    school_full_address = models.CharField(max_length=100, blank = False)
    school_ensemble_director = models.CharField(max_length=100, null=True,blank=True)
    private_teacher = models.CharField(max_length=100, null=True,blank=True)
    private_teacher_email = models.EmailField(max_length=100, null=True,blank=True)
    summer_programs = models.CharField(max_length=200, null=True,blank=True)
    read_agree_terms = models.CharField(max_length=1, choices=YES_NO, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s Application" % (self.app_student_id)
    
    
class ApplicationAdmin(models.Model):
    sua_app_id = models.ForeignKey(Application)
    submitted = models.BooleanField(default=True)
    approve_for_group = models.CharField(max_length=255, choices=ORCHESTRA_TYPE)
    date_approved = models.DateField(null=True,blank=True)
    approved_by = models.CharField(max_length=10,null=True,blank=True)
    paid = models.CharField(max_length=255, choices=PAID_STATUS,null=True,blank=True)
    paid_amount = models.FloatField(null=True,blank=True)
    paid_notes = models.CharField(max_length=200,null=True,blank=True)
    date_paid_in_full = models.DateField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s Admin" % self.sua_app_id.app_student_id
