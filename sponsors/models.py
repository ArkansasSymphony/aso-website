from django.db import models

class Sponsor(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	primary = models.BooleanField()
	education = models.BooleanField()
	url = models.CharField(max_length=255, null=True, blank=True)
	picture = models.ImageField(upload_to="sponsor_images", null=True, blank=True)
	
	
	def __unicode__(self):
		return "%(sponsor)s" % {'sponsor': self.name}
	