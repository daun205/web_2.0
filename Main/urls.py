from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
## FOR THE PATTERN
from django.conf.urls import *

import Main.views

views = Main.views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^404/$', views.debug404, name='debug404'),
]