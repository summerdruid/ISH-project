# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from viewer.models import Route, Run, Point

# Register your models here.
admin.site.register(Route)
admin.site.register(Run)
admin.site.register(Point)
