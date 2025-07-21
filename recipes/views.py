from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("HOME PAGE IS WORKING!")

def about(request):
    return HttpResponse("ABOUT PAGE IS WORKING!")

def contact(request):
    return HttpResponse("CONTACT PAGE IS WORKING!")

