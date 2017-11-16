# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Route(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Point(models.Model):
    longitude = models.IntegerField
    latitude = models.IntegerField

class Run(models.Model):
    route = models.ForeignKey(Route)
    points = models.ManyToManyField(Point)
    startTime = models.DateField()
