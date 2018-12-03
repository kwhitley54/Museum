# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request, 'pages/index.html')

def about(request):
    '''Loads the about page'''

    #return HttpResponse('about')




    return render(request, 'pages/about.html')

def questions(request):
   return render(request, 'pages/questions.html')


#
# # def search(request):
#     if request.method =='POST':
#         URL_SEARCH
#








def exhibit(request):
    return render(request, 'pages/exhibit.html')


def bob(request):
    return render(request, 'pages/bob.html')

def jackie(request):
    return render(request, 'pages/jackie.html')



def fredrick(request):
    return render(request, 'pages/fredrick.html')

def jordan(request):
    return render(request, 'pages/jordan.html')

def booker(request):
    return render(request, 'pages/booker.html')

def michael(request):
    return render(request, 'pages/michael.html')

def map(request):
    return render(request, 'pages/map.html')

def submit(request):
    return render(request, 'pages/submit.html')