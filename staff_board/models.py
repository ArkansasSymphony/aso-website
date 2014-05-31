from django.db import models

class Administrator(models.Model):

	TYPE_CHOICES = (
		('staff', 'staff'),
		('directors', 'directors'),
		('advisors', 'advisors'),
	)
	
	DEPARTMENT_CHOICES = (
		('administration', 'administration'),
		('artistic', 'artistic'),
		('operations', 'operations'),
		('development/marketing', 'development/marketing'),
		('education', 'education'),
	)
	
	BOARD_CHOICES = (
		('exec committee', 'exec committee'),
		('directors', 'directors'),
		('guild rep', 'guild rep'),
		('life', 'life'),
		('honorary', 'honorary'),
	)
	
	name = models.CharField(max_length="100", null=True, blank=False)
	order = models.IntegerField(null=True, blank=True)
	board_or_staff = models.CharField(max_length="50", choices=TYPE_CHOICES, null=True, blank=False)
	board_type = models.CharField(max_length="100", choices=BOARD_CHOICES, null=True, blank=True)
	department = models.CharField(max_length="50", choices=DEPARTMENT_CHOICES, null=True, blank=True)
	title = models.CharField(max_length="200", null=True, blank=True)
	email = models.CharField(max_length="254", null=True, blank=True)
	phone = models.CharField(max_length="22", null=True, blank=True)
	
	def __unicode__(self):
		return self.name
