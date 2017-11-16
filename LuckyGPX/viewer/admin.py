# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from viewer.models import Route, Run, Point, UserProfile

# Register your models here.
admin.site.register(Route)
admin.site.register(Run)
admin.site.register(Point)
admin.site.register(UserProfile)
