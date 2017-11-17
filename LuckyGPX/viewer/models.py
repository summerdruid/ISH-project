# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import xml.etree.ElementTree as ET

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Route(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner = models.ForeignKey(UserProfile, null=True)
    def __unicode__(self):
        return self.name

class Point(models.Model):
    longitude = models.IntegerField
    latitude = models.IntegerField

class Run(models.Model):
    route = models.ForeignKey(Route)
    points = models.ManyToManyField(Point)
    startTime = models.DateField(auto_now_add=True) #temp hack!!!


def addRunFromGPX(data, route):
    pdata = parseGPX(data)

    run = Run()
    run.route = route
    run.save()

    new_points = []
    for point in pdata:
        new_point = Point()
        new_point.latitude = point['lat']
        new_point.longitude = point['lon']
        new_points.append(new_point)
        new_point.save()

    run.points.add(*new_points)
    run.save()

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

