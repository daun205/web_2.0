from django.conf.urls import include, url
from django.contrib import admin

import Main.views

views = Main.views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
