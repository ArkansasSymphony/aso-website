from django.db import models

class Party(models.Model):
	ATTIRE_CHOICE = (
		('evening wear', 'evening wear'),
		('Saturday-Night-Out attire', 'Saturday-Night-Out attire'),
		('Casual attire', 'Casual attire'),
		('tea party attire', 'tea party attire'),
		)
	PRICE_CHOICE = (
		('$225 couple/$125 single', '$225 couple/$125 single'),
		('$50', '$50'),
		('$60', '$60'),
		('$40 per adult - children 12 and under included', '$40 per adult - children 12 and under included'),
		)

	name = models.CharField(max_length = 100, null = True, blank = False)
	short_description = models.CharField(max_length = 500, null = True, blank = True)
	long_description = models.TextField(null = True, blank = True)
	date = models.DateField()
	time = models.TimeField()
	display_date = models.CharField(max_length = 50, null = True, blank = False)
	display_time = models.CharField(max_length = 50, null = True, blank = False)
	attire = models.CharField(max_length = 100, choices = ATTIRE_CHOICE, null=True, blank = True)
	price = models.CharField(max_length = 200, choices = PRICE_CHOICE, null = True, blank = True)
	url_name = models.SlugField(max_length = 100)
	pe_id = models.IntegerField(max_length = 5, null = True, blank = True)

	def __unicode__(self):
		return "%(name)s" % {'name': self.name}

class Sponsor(models.Model):
	TYPE_CHOICE = (
		('premier', 'premier'),
		('patron', 'patron'),
		('participating', 'participating'),
		('builder', 'builder'),
		)

	sponsor_name = models.CharField(max_length = 250, null = True, blank = False)
	link = models.CharField(max_length = 255, null = True, blank = True)
	logo = models.ImageField(upload_to = "designerhouse/sponsor_images", null = True, blank = True)
	level = models.CharField(max_length = 100, choices = TYPE_CHOICE, null = True, blank = False)

	def __unicode__(self):
		return self.sponsor_name

class Designer(models.Model):

	designer_name = models.CharField(max_length = 250, null = True, blank = False)
	link = models.CharField(max_length = 255, null = True, blank = True)
	logo = models.ImageField(upload_to = "designer_images", null = True, blank = True)
	description = models.CharField(max_length = 1000, null = True, blank = True)

	def __unicode__(self):
		return self.designer_name
