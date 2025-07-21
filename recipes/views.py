from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html')

def about(request):
    return HttpResponse("ABOUT PAGE IS WORKING!")

def contact(request):
    return HttpResponse("CONTACT PAGE IS WORKING!")

