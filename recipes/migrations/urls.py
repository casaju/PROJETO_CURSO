
from django.urls import path
from django.http import HttpResponse
from recipes.views import home, about, contact

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    # Add more paths as needed
]