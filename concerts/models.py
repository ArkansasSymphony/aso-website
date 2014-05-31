from django.db import models

from arkansassymphony.people.models import Artist
from arkansassymphony.sponsors.models import Sponsor
from arkansassymphony.multimedia.models import Music, Video
from arkansassymphony.venue.models import Venue


class Show(models.Model):
	TYPE_CHOICES = (
	        ('classical', 'classical'),
	        ('pops', 'pops'),
	        ('chamber', 'chamber'),
		('nutcracker', 'nutcracker'),
		('event', 'event'),
		('other', 'other'),
		('youth', 'youth'),
		('neighborhood', 'neighborhood'),
		)

	SEASON_CHOICES = (
		('2010-2011', '2010-2011'),
		('2011-2012', '2011-2012'),
		('2012-2013', '2012-2013'),
		('2013-2014', '2013-2014'),
		('2014-2015','2014-2015'),
		)
    
	season = models.CharField(max_length=10, choices=SEASON_CHOICES)
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	artists = models.ManyToManyField(Artist, null=True, blank=True)
	conductor = models.CharField(max_length=100, null=True, blank=True)
	conductor_link = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	large_picture = models.ImageField(upload_to="show_images", null=True, blank=True)
	small_picture = models.ImageField(upload_to="show_images_small", null=True, blank=True)
	end_date = models.DateField()
	short_month = models.CharField(max_length=10)
	short_day = models.CharField(max_length=10)
	type = models.CharField(max_length=12, choices=TYPE_CHOICES)
	short_desc = models.TextField(null=True, blank=True)
	url_name = models.SlugField(max_length=100)
	sponsors = models.ManyToManyField(Sponsor, null=True, blank=True)
	music = models.ManyToManyField(Music, null=True, blank=True)
	video = models.ManyToManyField(Video, null=True, blank=True)

	def __unicode__(self):
		return "%(name)s" % {'name': self.name}
	
	class Meta:
		ordering = ('end_date',)
        

		
class Piece(models.Model):
	order = models.IntegerField(null=True, blank=True)
	composer = models.CharField(max_length=100, null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	program_note = models.TextField(null=True, blank=True)
	url_name = models.CharField(max_length=100)
	show = models.ForeignKey(Show, null=True, blank=True)
	music = models.ForeignKey(Music, null=True, blank=True)
	video = models.ForeignKey(Video, null=True, blank=True)
	
	def __unicode__(self):
		return "%(composer)s - %(title)s" % {'composer': self.composer, 'title': self.title}
	
	class Meta:
		ordering = ('order',)
	


class Concert(models.Model):
	show = models.ForeignKey(Show)
	date = models.DateTimeField(null=True, blank=True)
	time = models.CharField(max_length=100, null=True, blank=True)
	pe_id = models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return "%(show)s - %(date)s" % {'show': self.show.name, 'date': self.date}


class Subscription(models.Model):
	TYPE_CHOICES = (
	        ('classical', 'classical'),
	        ('pops', 'pops'),
	        ('chamber', 'chamber'),
		('neighborhood','neighborhood'),
		('flex', 'flex'),
	    )
	    
	type = models.CharField(max_length=12, choices=TYPE_CHOICES)
	name = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	shows = models.ManyToManyField(Show, null=True, blank=True)
	pe_id = models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}

