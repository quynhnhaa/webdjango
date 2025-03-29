from django.urls import path
from . import views

app_name="reviews"
urlpatterns = [
    path('', views.ViewIndex.as_view(), name="index"),
]
