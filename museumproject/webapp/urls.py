from django.conf.urls import url
from  . import views




urlpatterns = [
    url(r'^index',views.index, name = 'index'),
    url(r'^about',views.about, name = 'about'),
    url(r'^questions/$',views.questions, name='questions'),
    url(r'^exhibit/$', views.exhibit, name='exhibit'),
    url(r'^bob/$',views.bob, name='bob'),
    url(r'^jackie/$', views.jackie, name='jackie'),
    url(r'^fredrick',views.fredrick, name='fredrick'),
    url(r'^booker',views.booker, name='booker'),
    url(r'^jordan',views.jordan, name='jordan'),
    url(r'^michael',views.michael, name='michael'),

]



