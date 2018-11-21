from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def reg(request):
    template = loader.get_template('Reg.html')
    return HttpResponse(template.render())
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
