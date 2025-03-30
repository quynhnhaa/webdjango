from django.urls import path
from . import views

app_name="reviews"
urlpatterns = [
    path('review_create/<int:recipe_id>/', views.ReviewCreate.as_view(), name="review_create"),
]
