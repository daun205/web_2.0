# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Main.serializers import UserSerializer, GroupSerializer


#### not DRF related
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from Main.models import *
# import requests, json
from django.template import Context

def index(request):
    return HttpResponse(render(request, "Main/index.html"))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer