from django.db import models
from arkansassymphony import settings

class RSVP(models.Model):

	name = models.CharField(max_length = 100, null = True, blank = False)
	email = models.EmailField(null = True, blank = False)
	phone = models.CharField(max_length = 100, null = True, blank = True)
	address = models.CharField(max_length = 100, null = True, blank = False)
	city = models.CharField(max_length = 100, null = True, blank = False)
	state = models.CharField(max_length = 100, null = True, blank = False)
	zip = models.CharField(max_length = 100, null = True, blank = False)
	quantity = models.IntegerField(max_length = 100, null = True, blank = False)
	notes = models.TextField(null = True, blank = True)
   
	def __unicode__(self):
		return self.name