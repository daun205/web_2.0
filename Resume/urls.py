from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
## FOR THE PATTERN
from django.conf.urls import *

import Resume.views

views = Resume.views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]