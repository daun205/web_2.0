# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Main.serializers import UserSerializer, GroupSerializer


#### not DRF related
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from Main.models import *
# import requests, json
from django.template import Context

def index(request):
    return HttpResponse(render(request, "Main/index.html"))


def debug404(request):
    return HttpResponse(render(request, "404.html"))


def error404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

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