from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def jobForm (request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())

# Create your views here.
