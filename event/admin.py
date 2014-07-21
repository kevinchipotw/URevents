from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	class Meta:
		model = Event

admin.site.register(Event, EventAdmin)
