from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(User, default = User)
	pub_date = models.DateTimeField(default = datetime.datetime.now)
	event_date = models.DateTimeField('Event Date')
	body = models.TextField()

  
	def __unicode__(self):
		return smart_unicode(self.title)

