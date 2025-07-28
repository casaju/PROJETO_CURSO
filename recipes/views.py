from multiprocessing import context
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipe= Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe,
    })


def category(request, category_id):
    recipe= Recipe.objects.filter(category_id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipe,
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-page.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
# This view is for displaying a single recipe page.
# It uses the make_recipe function to generate a recipe object



