# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {}

    return render(request, 'viewer/index.html', context_dict)

def newindex(request):
    context_dict = {}

    return render(request, 'viewer/newindex.html', context_dict)

def test(request):
    context_dict = {'boldmessage':  "Bolf font message!"}

    return render(request, 'viewer/test.html', context_dict)
