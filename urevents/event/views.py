from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.utils import timezone
from .models import Event
from forms import EventForm
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

# Create your views here.



def home(request):
	args = {}
	args.update(csrf(request))

	args['events'] = Event.objects.order_by('event_date')

	return render_to_response("event_index.html", args)

def event(request, event_id= 1):
    return render_to_response('event.html',
                              {'event': Event.objects.get(id = event_id) })

def create(request):
	if request.POST: 
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect(reverse('event.views.home'))

	else:
		form = EventForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render_to_response('create_event.html', args)



