from django.db import models
from arkansassymphony.concerts.models import Show

class Comment(models.Model):
	name = models.CharField(max_length=100)
	message = models.TextField()
	posted = models.DateTimeField()
	show = models.ForeignKey(Show, blank=True, null=True)
	

	def __unicode__(self):
		return "%(name)s" % {'name': self.name}
