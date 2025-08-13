from django.test import TestCase
from django.urls import reverse


class RecipeURLsTests(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:recipes-home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category-category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_recipe_url_is_correct(self):
        url = reverse('recipes:recipe-recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')