from django.db import models
from arkansassymphony import settings

class Donation(models.Model):
	CHOICES = (
			('Yes', 'Yes'),
			('No', 'No')
		)

	name = models.CharField(max_length = 100, null = True, blank = False)
	donation = models.IntegerField(null = True, blank = False)
	anonymous = models.CharField(max_length = 5, choices = CHOICES, null = True, blank = False)
	email = models.EmailField(null = True, blank = False)
	phone = models.CharField(max_length = 100, null = True, blank = True)
	address = models.CharField(max_length = 100, null = True, blank = False)
	city = models.CharField(max_length = 100, null = True, blank = False)
	state = models.CharField(max_length = 100, null = True, blank = False)
	zip = models.CharField(max_length = 100, null = True, blank = False)
	notes = models.TextField(null = True, blank = True)

#	timestamp = models.DateTimeField('date added', auto_now_add = True)
	
	def __unicode__(self):
		return self.name
		
