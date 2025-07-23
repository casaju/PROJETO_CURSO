from multiprocessing import context
from django.shortcuts import render
from utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-page.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
# This view is for displaying a single recipe page.
# It uses the make_recipe function to generate a recipe object

