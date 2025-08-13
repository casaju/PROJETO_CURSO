from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeViewsTests(TestCase):
    def test_home_view_status_code(self):
        view =  resolve(reverse('recipes:recipes-home'))
        self.assertTrue(view.func ,  views.home)

    def test_category_view_status_code(self):
        view =  resolve(reverse('recipes:category-category', kwargs={'category_id': 1}))
        self.assertTrue(view.func ,  views.category)

    def test_detail_view_status_code(self):
        view =  resolve(reverse('recipes:recipe-recipe', kwargs={'id': 1}))
        self.assertTrue(view.func ,  views.recipe)