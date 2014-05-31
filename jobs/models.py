from django.db import models



class Job(models.Model):
	TYPE_CHOICES = (
	        ('admin', 'admin'),
	        ('orchestra', 'orchestra'),
		)

	type = models.CharField(max_length=10, choices=TYPE_CHOICES)
	active = models.BooleanField()
	title = models.CharField(max_length=100)
	posted = models.DateField()
	description = models.TextField(null=True, blank=True)
	url_name = models.SlugField(max_length=100)
	

	def __unicode__(self):
		return "%(title)s" % {'title': self.title}
	
	class Meta:
		ordering = ('posted',)
        

