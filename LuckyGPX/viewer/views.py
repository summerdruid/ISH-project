# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from viewer.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    context_dict = {}

    return render(request, 'viewer/index.html', context_dict)


# called user_login to avoid shadowing imported login function
def user_login(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your LuckyGPX account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'viewer/login.html', {})


# log out the user, checking that they are logged in
@login_required
def user_logout(request):
    logout(request)
    
    # send the user home
    return HttpResponseRedirect('/viewer')

@login_required
def restricted(request):
    return HttpResponse("You must log in to see this page.")

def register(request):

    # Boolean, False = user not registered, True = User registered
    registered = False

    # If we're receiving data, try to process it.
    if request.method == 'POST':
        # try to get data from the request
        user_form = UserForm(data=request.POST)

        # If the data was valid
        if user_form.is_valid():
            # Save to the database
            user = user_form.save()

            # Hash and save the password
            user.set_password(user.password)
            user.save()

            # User registered succesfully
            registered = True

        # Something went wrong, complain (to the user a well)
        else:
            print(user_form.errors)

    # we're not receiving data, so send them a form to fill in
    else:
        user_form = UserForm()

    # Render appropriate template
    return render(request,
            'viewer/register.html',
            {'user_form': user_form, 'registered': registered})


def newindex(request):
    context_dict = {}

    return render(request, 'viewer/newindex.html', context_dict)

def test(request):
    context_dict = {'boldmessage':  "Bolf font message!"}

    return render(request, 'viewer/test.html', context_dict)


def account(request):
	context_dict = {}

	return render(request, 'viewer/account.html', context_dict)

def editAccount(request):
	context_dict = {}

	return render(request, 'viewer/editAccount.html', context_dict)

def createRoute(request):
	context_dict = {}

	return render(request, 'viewer/createRoute.html', context_dict)

def loadRoute(request):
	context_dict = {}

	return render(request, 'viewer/loadRoute.html', context_dict)

def routeHistory(request):
	context_dict = {}

	return render(request, 'viewer/routeHistory.html', context_dict)

def viewGraphs(request):
	context_dict = {}

	return render(request, 'viewer/viewGraphs.html', context_dict)

def viewRoute(request):
	context_dict = {}

	return render(request, 'viewer/viewRoute.html', context_dict)
