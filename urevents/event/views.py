from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.utils import timezone
from .models import Event, Category, Organization
from forms import EventForm
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.db.models import Q, F

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.formtools.wizard.views import SessionWizardView

# Create your views here.



def home(request):
	return render_to_response("event_index.html",
		{'events': Event.objects.order_by('event_date'),
		 'categories': Category.objects.order_by('title')},
			context_instance = RequestContext(request) )


def event(request, event_id= 1):
    return render_to_response('event_detail.html',
                              {'event': Event.objects.get(id = event_id)},
                              context_instance = RequestContext(request) )


def create(request):
	if request.POST: 
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect(reverse('event.views.home'))

	else:
		form = EventForm()

	return render_to_response('create_event.html', {'form': form},
														context_instance = RequestContext(request))


def search(request):

	query = request.GET.get('q', '')
	results = Event.objects.order_by('event_date')

	if query:
		results = Event.objects.filter( Q(title__icontains = query)|
			Q(pub_date__icontains = query)| Q(event_date__icontains = query)|
			Q(location__icontains = query)| Q(body__icontains = query)|
			Q(author__username__icontains = query )| Q(category__title__icontains = query)|
			Q(co_sponsored__title__icontains = query)
			).distinct()

	return render_to_response('search.html',
							  {'query': query,
							   'results': results, 
							   'categories': Category.objects.order_by('title')},
							   context_instance = RequestContext(request))
	

def category_filter(request):
	
	query = request.GET.get('q', '')
	results = []

	if query:

		results = Event.objects.filter(Q(category__title__icontains = query)).distinct()

	return render_to_response('categorize.html', 
						  {'query': query,
						   'results': results,
						   'categories': Category.objects.order_by('title')},
						   context_instance = RequestContext(request))

