from django.conf.urls import patterns, include, url

from django.conf import settings 
from django.conf.urls.static import static 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'event.views.home', name = 'home'),
	url(r'^event(?P<event_id>\d+)/$','event.views.event', name = 'event'), 
	url(r'^event/create/$', 'event.views.create', name = 'create'), 
	url(r'^event/search/$', 'event.views.search', name = 'search'),
	url(r'^event/category_filter/$', 'event.views.category_filter', name = 'category_filter'),


	#user authentication
    
  url(r'^accounts/auth/$', 'urevents.views.auth_view'), 
  url(r'^accounts/logout/$', 'urevents.views.logout', name = 'logout'), 



)