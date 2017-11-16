# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from viewer.forms import UserForm
import xml.etree.ElementTree as ET


def index(request):
    context_dict = {}

    return render(request, 'viewer/index.html', context_dict)


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
            print user_form.errors

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


# takes gpx data as a string, returns list of dictionaries with
# lat and long of each point on the first track of the gpx data.
def parseGPX(data):
    gpxstring = data

    namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    root = ET.fromstring(gpxstring)
    track = root.findall(".//gpx:trk", namespace)
    trkseg  = root.find(".//gpx:trkseg", namespace)
    points = trkseg.findall(".gpx:trkpt", namespace)
    parsed_data = []
    for point in points:
        lat = float(point.attrib['lat'])
        lon = float(point.attrib['lon'])
        parsed_data.append({'lat': lat, 'lon': lon})

    return parsed_data
        

