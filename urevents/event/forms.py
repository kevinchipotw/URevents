from django import forms
from models import Event

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ('title', 'author', 'pub_date', 'event_date', 'body')

