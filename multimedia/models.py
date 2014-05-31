from django.db import models


class Music(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	internal = models.BooleanField()
	filename = models.FileField(upload_to="music", null=True, blank=True)
	url = models.CharField(max_length=255, null=True, blank=True)
	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}


class Video(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	internal = models.BooleanField()
	filename = models.FileField(upload_to="video", null=True, blank=True)
	url = models.CharField(max_length=255, null=True, blank=True)
	
	def __unicode__(self):
		return "%(name)s" % {'name': self.name}
	
