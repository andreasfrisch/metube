from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    template = "index.html"
    context = {}
    return render_to_response(template, context, context_instance=RequestContext(request))
	