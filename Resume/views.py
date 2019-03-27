from django.shortcuts import render



#### not DRF related
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from Resume.models import *
# import requests, json
from django.template import Context
# Create your views here.

def index(request):
    return HttpResponse(render(request, "Main/resume_daun.html"))


def debug404(request):
    return HttpResponse(render(request, "404.html"))


def error404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response
