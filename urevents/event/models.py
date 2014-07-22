from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length = 250)
	description = models.TextField()

	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"

	def __unicode__(self):
		return self.title

class Organization(models.Model):
	title = models.CharField(max_length = 250)
	description = models.TextField()

	class Meta:
		ordering = ['title']

	def __unicode__(self):
		return self.title


class Event(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey(User, default = User)
	pub_date = models.DateTimeField(default = datetime.datetime.now)
	event_date = models.DateTimeField('Event Date')
	category = models.ManyToManyField(Category)
	co_sponsored = models.ManyToManyField(Organization)
	location = models.TextField()
	body = models.TextField()

  
	def __unicode__(self):
		return smart_unicode(self.title)

