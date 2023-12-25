from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def details(request):
    template = loader.get_template('details\index.html')
    return HttpResponse(template.render())
