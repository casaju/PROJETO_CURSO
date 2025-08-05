from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    if not recipe:
        raise get_object_or_404(Recipe, pk=category_id, is_published=True)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipe,
        'title': f'{recipe.first().category.name} - Category | '
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(request, 'recipes/pages/recipe-page.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
# This view is for displaying a single recipe page.
# It uses the make_recipe function to generate a recipe object



