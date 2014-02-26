from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import *

def about(request):
    #html = "<html><body>It is now %s.</body></html>" % now
    print "testdfdsfsdf"    
    #t = loader.get_template('home.html')
    #return HttpResponse(t.render)
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response("templates/home.html")

def profile(request):
    now = datetime.datetime.now()
    template = "templates/profile.html"
    return render_to_response(template, {'Time': now})