from django.urls import path
from recipes import views

app_name = 'recipes' # Namespace for the app

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/category/<int:category_id>/', views.category, name='category-category'),
    path('recipes/<int:id>/', views.recipe, name='recipe-recipe'),
]