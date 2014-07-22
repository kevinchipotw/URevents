from django.contrib import admin
from .models import Event, Category, Organization

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)


class OrganizationAdmin(admin.ModelAdmin):
	class Meta:
		model = Organization

admin.site.register(Organization, OrganizationAdmin)


class EventAdmin(admin.ModelAdmin):
	class Meta:
		model = Event

admin.site.register(Event, EventAdmin)


