from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	website = models.CharField(max_length=255, null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	picture = models.ImageField(upload_to="artist_images", null=True, blank=True)
	url_name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "%(artist)s" % {'artist': self.name}

	class Meta:
		ordering = ('id',)
 


class Instrument(models.Model):
	name = models.CharField(max_length=100)
	list_order = models.IntegerField()
	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}


class Player(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	instrument = models.ForeignKey(Instrument)
	section_order = models.IntegerField()
	chair_name = models.CharField(max_length=100, null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	picture = models.ImageField(upload_to="orchestra_images", null=True, blank=True)

	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}
