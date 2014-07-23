from django.conf.urls import patterns, include, url

from django.conf import settings 
from django.conf.urls.static import static 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^$', 'event.views.home', name = 'home'),
	url(r'^event(?P<event_id>\d+)/$','event.views.event', name = 'event'), 
	url(r'^create/$', 'event.views.create', name = 'create'), 
	url(r'^search/$', 'event.views.search', name = 'search'),

	url(r'^admin/', include(admin.site.urls)),


)