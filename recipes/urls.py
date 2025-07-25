from django.urls import path
from recipes import views

app_name = 'recipes' # Namespace for the app

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/<int:id>/', views.recipe, name='recipe-recipe' ),
]