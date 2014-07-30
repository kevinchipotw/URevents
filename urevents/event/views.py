from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.utils import timezone
from .models import Event, Category, Organization
from forms import EventForm, CategoryForm
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.db.models import Q, F
import datetime
from datetime import date, timedelta, time
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import FormView

# Create your views here.


def home(request):
	event = Event.objects.filter(event_date__lte =datetime.datetime.now())
	event.delete()

	form = CategoryForm(request.POST, request.FILES)

	event_list = Event.objects.order_by('event_date')
	paginator = Paginator(event_list, 5)
	page = request.GET.get('page')
	try:
		events = paginator.page(page)
	except PageNotAnInteger:
		events = paginator.page(1)# If page is not an integer, deliver first page.
	except EmptyPage:
		events = paginator.page(paginator.num_pages) # If page is out of range (e.g. 9999), deliver last page of results.
	
	return render_to_response('event_index.html', {
		'form': form,
		'events': events,
		 'categories': Category.objects.order_by('title'),
		 'organizations': Organization.objects.order_by('title')},
			context_instance = RequestContext(request) )




def event(request, event_id= 1):
		return render_to_response('event_detail.html',
															{'event': Event.objects.get(id = event_id),
															'categories': Category.objects.order_by('title')},
															context_instance = RequestContext(request) )


def create(request):
	if request.POST: 
		form = EventForm(request.POST, request.FILES)

		if form.is_valid():
			Event = form.save(commit=False)
			Event.author = request.user
			Event.pub_date = datetime.datetime.now()
			Event = Event.save()
			form.save_m2m()

			return HttpResponseRedirect(reverse('event.views.home'))

	else:
		form = EventForm()


	eighthour_advanced = datetime.datetime.now()+timedelta(hours=8)
	d = eighthour_advanced.strftime("%Y-%m-%d %H:%M")

	return render_to_response('create_event.html', 
														{'form': form,
														'organizations': Organization.objects.order_by('title'),
														'categories': Category.objects.order_by('title'),
														'users': User.objects.order_by('username'),
														'time2': d },
														context_instance = RequestContext(request))


#@login_required
def edit(request, id=None, template_name='edit_event.html', event_id = 1):

	event = Event.objects.get(id = event_id)

	if event.author != request.user:
		messages.info(request, 'You need to be the author to edit the post.')
		return HttpResponseRedirect(reverse('event.views.home'))

	form = EventForm(instance=event)
	event1 = Event.objects.filter(id = event_id)
	event1.delete()

	return render_to_response(template_name, {
			'form': form,
	}, context_instance=RequestContext(request))


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




def search_filter(request):
	query = request.GET.get('q', '')
	results = []

	if query:
		results = Event.objects.filter(Q(category__title__icontains = query)|
			Q(author__username__icontains = query)|Q(co_sponsored__title__icontains = query)
			).distinct()

	return render_to_response('categorize.html', 
							{'query': query,
							 'results': results,
							 'categories': Category.objects.order_by('title')},
							 context_instance = RequestContext(request))




def aboutus(request):
	return render_to_response('about_us.html',
		context_instance = RequestContext(request))

def contactus(request):
	return render_to_response('contact_us.html',
		context_instance = RequestContext(request))




