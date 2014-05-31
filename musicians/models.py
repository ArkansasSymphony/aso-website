from django.db import models
from arkansassymphony.musicians.model_multi import *
#from arkansassymphony.concerts.models import Show

class HRDocument(models.Model):
	name = models.CharField(max_length = 200, null = True, blank = False)
	description = models.TextField(max_length = 500, null = True, blank = True)
	file = models.FileField(upload_to = "hr_docs", null = True, blank = False)

	def __unicode__(self):
		return self.name

class Venue(models.Model):
	VENUE_TYPES = (
		('orchestra', 'orchestra'),
		('chamber', 'chamber'),
		)

	name = models.CharField(max_length = 200, null = True, blank = False)
	map_link = models.TextField(max_length = 1000, null = True, blank = True)
	map_image = models.ImageField(upload_to="musician_images", null = True, blank = True)
	phone = models.CharField(max_length = 50, null = True, blank = True)
	link_1 = models.URLField(null = True, blank = True)
	link_2 = models.URLField(null = True, blank = True)
	address = models.CharField(max_length = 400, null = True, blank = False)
	city = models.CharField(max_length = 100, null = True, blank = False)
	state = models.CharField(max_length = 2, null = True, blank = False)
	zip_code = models.IntegerField(max_length = 10, null = True, blank = False)
	venue_type = models.CharField(max_length = 50, choices = VENUE_TYPES, null = True, blank = False)
	url_name = models.SlugField(max_length = 200, null = True, blank = False)
	notes = models.TextField(max_length = 500, null = True, blank = True)
	
	def __unicode__(self):
		return self.name


class Concert(models.Model):
	TYPE_CHOICES = (
	    ('classical', 'classical'),
	    ('pops', 'pops'),
	    ('I.N.C.', 'I.N.C.'),
	    ('chamber', 'chamber'),
		('other chamber', 'other chamber'),
		('ASO quartet', 'ASO quartet'),
		('other', 'other'),
		)

	SEASON_CHOICES = (
		('2012-2013', '2012-2013'),
		('2013-2014', '2013-2014'),
		('2014-2015', '2014-2015'),
		('2015-2016', '2015-2016'),
		)
    
	BUS_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	
	COMP_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	
	season = models.CharField(max_length = 10, choices = SEASON_CHOICES)
	name = models.CharField(max_length = 100)
	conductor = models.CharField(max_length = 100, null = True, blank = True)
	end_date = models.DateField()
	long_date = models.CharField(max_length = 100, null = True, blank = True)
	long_time = models.CharField(max_length = 100, null = True, blank = True)
	type = models.CharField(max_length = 50, choices = TYPE_CHOICES)
	url_name = models.SlugField(max_length = 200, null = True, blank = False)
	venue = models.ForeignKey(Venue, null = True, blank = True)
	comps_available = models.CharField(max_length = 10, choices = COMP_CHOICES, null = True, blank = False)
	bus_service = models.CharField(max_length = 10, choices = BUS_CHOICES, null = True, blank = False)
	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}

class Schedule(models.Model):
	
	schedule_item = models.CharField(max_length = 200, null = True, blank = True)
	show = models.ForeignKey(Concert, null = True, blank = False)
	order = models.IntegerField(max_length = 10, null = True, blank = True)
	
	def __unicode__(self):
		return self.schedule_item
		
class ConcertDocument(models.Model):
	name = models.CharField(max_length = 200, null = True, blank = True)
	file = models.FileField(upload_to = "concert_documents", null = True, blank = True)
	show = models.ForeignKey(Concert, null = True, blank = True)
	
	def __unicode__(self):
		return self.name
		
class ProgramItem(models.Model):
	composer = models.CharField(max_length = 200, null = True, blank  = True)
	title = models.CharField(max_length = 200, null = True, blank = True)
	show = models.ForeignKey(Concert, null = True, blank = True)
	instrumentation = models.CharField(max_length = 200, null = True, blank = True)
	notes = models.TextField(null = True, blank = True) 
	order = models.IntegerField(null = True, blank = True)
	
	def __unicode__(self):
		return self.title	
		
class Service(models.Model):
		
	SERVICE_CHOICES = (
	('Rehearsal', 'Rehearsal'),
	('Performance', 'Performance'),
	)
	
	name = models.CharField(max_length = 100, null=True, blank=False)
	show = models.ForeignKey(Concert, null=True, blank=False)
	venue = models.ForeignKey(Venue, null = True, blank = True)
	date = models.DateField()
	display_time = models.CharField(max_length = 100, null=True, blank=True)
	time = models.TimeField(max_length = 50, null=True, blank = False)
	service_type = models.CharField(max_length = 50, choices=SERVICE_CHOICES, null=True, blank=False)
	service_note = models.CharField(max_length = 200, null = True, blank = True)

	def __unicode__(self):
		return self.name
		
class WageChart(models.Model):

	fiscal_year = models.CharField(max_length = "20", null = True, blank = False)
	principal_performance = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	principal_rehearsal = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	section_performance = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	section_rehearsal = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	mileage = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	doubling = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	breakfast = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	lunch = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	dinner = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	travel_long = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	travel_short = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	double_service = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	per_diem_single = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	per_diem_double = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	aso_ensembles = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	standard_cartage = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	marimba_cartage = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	vibes_cartage = models.DecimalField(decimal_places = 2, max_digits = 20, null = True, blank = False)
	
	def __unicode__(self):
		return self.fiscal_year

class BusStop(models.Model):
	stop = models.CharField(max_length = 200, null = True, blank = False)
	show = models.ForeignKey(Concert, null = True, blank = False)
	
	def __unicode__(self):
		return self.stop
		
#--------------------------------------------            classes for forms           --------------------------------------------------	
class HotelForm(models.Model):

	ROOM_CHOICES = (
	('single', 'single'),
	('double', 'double'),
	)
		
	name = models.CharField(max_length=100, null = True, blank = False)
	email = models.EmailField()
	check_in = models.DateField()
	check_out = models.DateField()
	room_type = models.CharField(max_length = 20, choices=ROOM_CHOICES, null = True, blank = True)
	roommate_request = models.CharField(max_length=100, null = True, blank = True)

class BusForm(models.Model):
	RIDING_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No'),
		)
	MEAL_CHOICES = (
		('Regular', 'Regular'),
		('Vegetarian', 'Vegetarian'),
		('No meal', 'No meal'),
		)
		
	name = models.CharField(max_length = 100, null = True, blank = False)
	email = models.EmailField()
	riding = models.CharField(max_length = 20, choices = RIDING_CHOICES, null = True, blank = True)
	boarding = models.ForeignKey(BusStop, null = True, blank = True)
	meal = models.CharField(max_length = 20, choices = MEAL_CHOICES, null = True, blank = True)
	
	def __unicode__(self):
		return self.name
		
class CompTicket(models.Model):
	DAY_CHOICES = (
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday'),
		('Other - please explain', 'Other - please explain'),
		)
		
	DELIVERY_CHOICES = (
		('will-call', 'will-call'),
		('deliver at rehearsal', 'deliver at rehearsal'),
		)
		
	musician_name = models.CharField(max_length = 50, null = True, blank = False)
	email = models.EmailField()
	show = models.ForeignKey(Concert, null = True, blank = False)
	day = models.CharField(max_length = 40, choices = DAY_CHOICES, null = True, blank = False)
	quantity = models.IntegerField(max_length = 10, null = True, blank = False)
	delivery = models.CharField(max_length = 100, choices = DELIVERY_CHOICES, null = True, blank = False)
	notes = models.TextField(null = True, blank = True)
	
	def __unicode__(self):
		return self.musician_name
		
class AdminClaimForm(models.Model):
	
	TRIP_CHOICES = (
	('one way', 'one way'),
	('round trip', 'round trip'),
	)
	
	FORM_CHOICES = (
	('Standard', 'Standard'),
	('Quartet/Chamber/Outreach', 'Quartet/Chamber/Outreach'),
	)
	
	DIEM_CHOICES = (
	('Single performance', 'Single performance'),
	('Double performance', 'Double performance'),
	('Quartet only - breakfast', 'Quartet only - breakfast'),
	('Quartet only - lunch', 'Quartet only - lunch'),
	('Quartet only - dinner', 'Quartet only - dinner'),
	)
	
	CARTAGE_CHOICES = (
	('Harp', 'Harp '),
	('Harpsichord ', 'Harpsichord '),
	('Electric Keyboards ', 'Electric Keyboards '),
	('Xylophone ', 'Xylophone '),
	('Timpani ', 'Timpani '),
	('Bass Drum ', 'Bass Drum '),
	('Drum Set ', 'Drum Set '),
	('Electric Guitar or Bass/amp ', 'Electric Guitar or Bass/amp '),
	('Marimba', 'Marimba'),
	('Vibes', 'Vibes'),
	)

	form_type = models.CharField(max_length=50, choices=FORM_CHOICES, null = True, blank=False)
	name = models.CharField(max_length=50, blank=False)
	service = models.ForeignKey(Concert, null = True, blank = False)
	other_service = models.CharField(max_length=50, blank = True)
	email = models.EmailField()
	leg1a = models.CharField(max_length=50, null = True, blank=True)
	leg1b = models.CharField(max_length=50, null = True, blank=True)
	leg2a = models.CharField(max_length=50, null = True, blank=True)
	leg2b = models.CharField(max_length=50, null = True, blank=True)
	leg3a = models.CharField(max_length=50, null = True, blank=True)
	leg3b = models.CharField(max_length=50, null = True, blank=True)
	leg4a = models.CharField(max_length=50, null = True, blank=True)
	leg4b = models.CharField(max_length=50, null = True, blank=True)
	leg5a = models.CharField(max_length=50, null = True, blank=True)
	leg5b = models.CharField(max_length=50, null = True, blank=True)
	leg6a = models.CharField(max_length=50, null = True, blank=True)
	leg6b = models.CharField(max_length=50, null = True, blank=True)

	round1 = models.BooleanField(blank = True) 
	round2 = models.BooleanField(blank = True)
	round3 = models.BooleanField(blank = True)
	round4 = models.BooleanField(blank = True)
	round5 = models.BooleanField(blank = True)
	round6 = models.BooleanField(blank = True)

	date1 = models.CharField(max_length=50, null = True, blank = True)
	date2 = models.CharField(max_length=50, null = True, blank = True)
	date3 = models.CharField(max_length=50, null = True, blank = True)
	date4 = models.CharField(max_length=50, null = True, blank = True)
	date5 = models.CharField(max_length=50, null = True, blank = True)
	date6 = models.CharField(max_length=50, null = True, blank = True)

	principal_instrument = models.CharField(max_length=50, null = True, blank=True)
	double_1 = models.CharField(max_length=50, null = True, blank=True)
	double_2 = models.CharField(max_length=50, null = True, blank=True)
	double_3 = models.CharField(max_length=50, null = True, blank=True)
	double_4 = models.CharField(max_length=50, null = True, blank=True)
	service_number = models.IntegerField(max_length = 10, null = True, blank=True)
	cartage = MultiSelectField(max_length = 50, choices = CARTAGE_CHOICES, null = True, blank=True)
	diem_type = MultiSelectField(max_length=50, choices=DIEM_CHOICES, null = True, blank=True)
	comments = models.TextField(null = True, blank=True)
	mileage_miles = models.CharField(max_length = 50, null = True, blank = True)
	mileage_claim = models.CharField(max_length = 50, null = True, blank = True)
	doubling_claim = models.CharField(max_length = 50, null = True, blank = True)
	cartage_claim = models.CharField(max_length = 50, null = True, blank = True)
	diem_claim = models.CharField(max_length = 50, null = True, blank = True)
	total_claim = models.CharField(max_length = 50, null = True, blank = True)

	def __unicode__(self):
		return self.name
		
