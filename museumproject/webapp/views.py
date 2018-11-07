# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    #return('HELLO FROM POSTS   ')

    return render(request, 'pages/index.html')

def about(request):
    '''Loads the about page'''

    co


    return render(request, 'pages/about.html',context)

