from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve, response
from recipes import views
from recipes import models
from recipes.models import Recipe, Category, User



class RecipeViewsTests(TestCase):
    def test_home_view_status_code(self):
        view =  resolve(reverse('recipes:recipes-home'))
        self.assertTrue(view.func ,  views.home)
    
    def test_home_view_loads_correct_template(self):
        category = Category.objects.create(name='Test Category')
        author= User.objects.create(
            first_name='Test',
            first_name='author',
            username= 'user',
            password='pass',
            email='user@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Portions',
            preparation_step='Recipe Preparation Steps',
            preparation_step_is_html = False,
            is_published = True,
        )

    def test_category_view_status_code(self):
        view =  resolve(reverse('recipes:category-category', kwargs={'category_id': 1}))
        self.assertTrue(view.func ,  views.category)

    def test_recipe_category_view_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category-category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_status_code(self):
        view =  resolve(reverse('recipes:recipe-recipe', kwargs={'id': 1}))
        self.assertTrue(view.func ,  views.recipe)

    def test_recipe_detail_view_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe-recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_view_status_code(self):
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipes-home'))
        self.assertContains(response, 'No recipes found')