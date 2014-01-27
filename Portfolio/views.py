from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def about(request):
    #html = "<html><body>It is now %s.</body></html>" % now
    template = "home.html"
    #return HttpResponse(html)
    return render_to_response(template)

def profile(request):
    now = datetime.datetime.now()
    template = "profile.html"
    print "this is the test"
    return render_to_response(template, {'Time': now})