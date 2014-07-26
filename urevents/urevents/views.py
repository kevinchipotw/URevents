from django.shortcuts import render_to_response
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    
    if user is not None:
    	if user.is_active:
	        auth.login(request, user)
	        return HttpResponseRedirect(reverse('event.views.home'))

    else:
        messages.success(request, 'Login information is invalid. Please try again.')

        return HttpResponseRedirect(reverse('event.views.home'))



def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('event.views.home'))

