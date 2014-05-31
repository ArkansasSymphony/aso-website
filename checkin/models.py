from django.db import models
from arkansassymphony import settings

class Patron(models.Model):
	CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	
	first_name = models.CharField(max_length = 100, null = True, blank = True)
	last_name = models.CharField(max_length = 100, null = True, blank = False)
	full_name = models.CharField(max_length = 100, null = True, blank = True)
	email = models.EmailField(null = True, blank = True)
	organization = models.CharField(max_length =200, null = True, blank = True)
	bid_number = models.CharField(max_length = 100, null = True, blank = True)
	checked_in = models.CharField(max_length = 10, choices = CHOICES, null = True, blank = True)
	cc_number = models.CharField(max_length = 100, null = True, blank = True)
	cc_month = models.IntegerField(null = True, blank = True)
	cc_year = models.IntegerField(null = True, blank = True)
	cc_cvc = models.CharField(max_length = 100, null = True, blank = True)
	stripe_id = models.CharField(max_length = 100, null = True, blank = True)
	phone = models.CharField(max_length = 100, null = True, blank = True)
	address = models.CharField(max_length = 100, null = True, blank = True)
	city = models.CharField(max_length = 100, null = True, blank = True)
	state = models.CharField(max_length = 100, null = True, blank = True)
	zip = models.CharField(max_length = 100, null = True, blank = True)
	dining_assignment = models.CharField(max_length = 100, null = True, blank = True)
	notes = models.TextField(null = True, blank = True)
   
	def __unicode__(self):
		return self.full_name
		
class Charge(models.Model):
	PAYMENT_CHOICES = (
		('Check', 'Check'),
		('Cash', 'Cash'),
		('Card', 'Card'),
		('Other', 'Other')
	)
	
	description = models.CharField(max_length = 250, null = True, blank = False)
	item_number = models.CharField(max_length = 25, null = True, blank = True)
	price = models.IntegerField(null = True, blank = False)
	customer = models.ForeignKey(Patron, null=True, blank=False)
	payment_method = models.CharField(max_length = 100, choices = PAYMENT_CHOICES, null = True, blank = False)
	notes = models.TextField(null = True, blank = True)
	
	def __unicode__(self):
		return self.description
		
