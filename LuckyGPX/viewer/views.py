# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}

    return render(request, 'viewer/index.html', context_dict)
