from django.db import models

class Venue(models.Model):

	TYPE_CHOICES = (
		('masterworks', 'masterworks'),
		('pops', 'pops'),
		('chamber', 'chamber'),
		('inc', 'inc'),
		('other', 'other'),
	)
	STATUS_CHOICES = (
		('active', 'active'),
		('inactive', 'inactive'),
	)

	name = models.CharField(max_length="100", null=True, blank=False)
	status = models.CharField(max_length="25", choices=STATUS_CHOICES, null = True, blank = False)
	venue_type = models.CharField(max_length="25", choices=TYPE_CHOICES, null=True, blank=False)
	map_link = models.CharField(max_length="1000", null=True, blank=True)
	alt_map_link = models.CharField(max_length="1000", null = True, blank = True)
	embed_link = models.CharField(max_length="1000", null=True, blank=True)
	first_from = models.CharField(max_length=100, null = True, blank = True)
	second_from = models.CharField(max_length=100, null = True, blank = True)
	first_directions = models.TextField(null = True, blank = True)
	second_directions = models.TextField(null = True, blank = True)
	venue_seats = models.ImageField(upload_to="venue_images", null = True, blank = True)
	venue_image = models.ImageField(upload_to="venue_images", null = True, blank = True)
	address = models.CharField(max_length="100", null = True, blank = True)
	phone = models.CharField(max_length="25", null = True, blank = True)
	city = models.CharField(max_length="100", null = True, blank = True)
	state = models.CharField(max_length="100", null = True, blank = True)
	zip_code = models.CharField(max_length="20", null = True, blank = True)
	url_name = models.SlugField(max_length=100)
	
	def __unicode__(self):
		return self.name
