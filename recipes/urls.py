from django.urls import path
from . import views

app_name="recipes"
urlpatterns = [
    path('', views.ViewIndex.as_view(), name="index"),
    path('recipe_detail/<int:recipe_id>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('recipe_edit/<int:recipe_id>/', views.RecipeEdit.as_view(), name="recipe_edit"),
    path("recipe_create/", views.RecipeCreate.as_view(), name="recipe_create"),
    path("recipe_list/", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe_search_name/", views.RecipeListSearchName.as_view(), name="recipe_search_name"),
    # path("recipe_search_category/", views.RecipeListSearchCategory.as_view(), name="recipe_search_category"),
    path('showimage/', views.ShowImage.as_view(), name="showimage"),
    path("clear_recipe_success/", views.clear_recipe_success, name="clear_recipe_success"),
    path("recipe_personal/", views.RecipePersonal.as_view(), name="recipe_personal"),
]
