from django.urls import path
from . import views
app_name="users"
urlpatterns = [
    path('', views.ViewIndex.as_view(), name="index"),
]
