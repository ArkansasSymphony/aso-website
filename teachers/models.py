from django.db import models
from arkansassymphony import settings

class Teacher(models.Model):
	INSTRUMENTS = (
		('violin','violin'),
		('viola','viola'),
		('cello','cello'),
		('bass','bass'),
		('flute','flute'),
		('oboe','oboe'),
		('english horn', 'english horn'),
		('bassoon','bassoon'),
		('clarinet','clarinet'),
		('saxophone', 'saxophone'),
		('horn','horn'),
		('trumpet', 'trumpet'),
		('trombone', 'trombone'),
		('tuba', 'tuba'),
		('percussion', 'percussion'),
		('harp', 'harp'),
		('piano', 'piano'),
		)
	name = models.CharField(max_length = 100, null = True, blank = False)
	email = models.EmailField(null = True, blank = False)
	phone = models.CharField(max_length = 100, null = True, blank = True)
	instrument = models.CharField(max_length = 100, choices=INSTRUMENTS, null = True, blank = False)
	notes = models.TextField(null = True, blank = True)
	order = models.IntegerField(null = True, blank = True)
   
	def __unicode__(self):
		return self.name
