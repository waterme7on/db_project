from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    template = loader.get_template('BaseIndex.html')
    context = {}
    return HttpResponse(template.render(context, request))