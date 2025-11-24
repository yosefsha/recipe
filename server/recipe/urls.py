from django.urls import path
from recipe import views    
app_name = 'recipe'
urlpatterns = [
    path('', views.RecipeListView.as_view(), name='list'),  # /api/recipe/
    path('<int:pk>/', views.RecipeDetailView.as_view(), name='detail'),  # /api/recipe/<id>/
    path('create/', views.RecipeCreateView.as_view(), name='create'),  # /api/recipe/create/
    
]