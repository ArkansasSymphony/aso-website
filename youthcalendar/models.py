from django.db import models

class Event(models.Model):
        ORCHESTRA_CHOICES = (
                ('preparatory', 'preparatory'),
                ('prelude', 'prelude'),
                ('academy', 'academy'),
		('youth', 'youth'),
		('all', 'all'),
            )

	name = models.CharField(max_length=100)
        date = models.DateField()
	time = models.CharField(max_length=100, null=True, blank=True)
	location = models.CharField(max_length=100, null=True, blank=True)
        group = models.CharField(max_length=50, choices=ORCHESTRA_CHOICES)
	description = models.TextField(null=True, blank=True)


        def __unicode__(self):
                return "%(name)s - %(date)s" % {'name': self.name, 'date': self.date}

        class Meta:
                ordering = ('date',)

