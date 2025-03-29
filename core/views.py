from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
# Create your views here.


class HomeView(View):
    def get(self, request):
        recipe = Recipe.objects.first() 
        return render(request, "homepage/index.html", {"recipe": recipe})