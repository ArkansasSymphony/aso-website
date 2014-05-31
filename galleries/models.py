from django.db import models
from arkansassymphony.people.models import Artist
from arkansassymphony.galleries.thumbs import ImageWithThumbsField

class Gallery(models.Model):

	name = models.CharField(max_length=100, null=True, blank=False)
	artists = models.ManyToManyField(Artist, null=True, blank=True)
	conductor = models.CharField(max_length=100, null=True, blank=True)
	conductor_link = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	date = models.CharField(max_length=100, null=True, blank=True)
	order_date = models.DateField()
	cover_photo = ImageWithThumbsField(upload_to='galleries/cover_photos', sizes=((250,250),), blank=True)
	url_name = models.SlugField(max_length=100)

	def __unicode__(self):
		return self.name

class Audio(models.Model):
	name = models.CharField(max_length = 100, null = True, blank = False)
	embed_link = models.CharField(max_length=1000, null = True, blank = False)	
	
	def __unicode__(self):
		return self.name
	
class Photo(models.Model):
	COVER_CHOICES = (
		('yes', 'yes'),
		('no', 'no'),
	)
	
	gallery = models.ForeignKey(Gallery)
	photo_id = models.CharField(max_length=20, null=True, blank=True)
	photo = ImageWithThumbsField(upload_to='galleries', sizes=((100,100),))#resizes for thumbnail
	short_desc = models.CharField(max_length=200, null=True, blank=True)
	
	def __unicode__(self):
		return self.photo_id
