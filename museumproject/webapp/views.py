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



def example(request):
    return render(request, 'pages/example.html')
