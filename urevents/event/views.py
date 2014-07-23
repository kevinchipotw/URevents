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

# Create your views here.



def home(request):
	args = {}
	args.update(csrf(request))

	args['events'] = Event.objects.order_by('event_date')
	args['categories'] = Category.objects.order_by('title')

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


def search(request):

	query = request.GET.get('q', '')

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
							   'categories': Category.objects.order_by('title') })
	

def category_filter(request):
	
	query = request.GET.get('q', '')

	if query:
		results = Event.objects.filter(Q(category__title__icontains = query)).distinct()

	return render_to_response('search.html', 
						  {'query': query,
						   'results': results })


