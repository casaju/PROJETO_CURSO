from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html', context= {'name': 'Júlia Casagrande'})

def recipes(request,id):
    return render(request, 'recipes/pages/recipe-page.html', context= {'name': 'Júlia Casagrande'})

