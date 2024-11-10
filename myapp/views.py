from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("I made this website, i think it updates as i go")
