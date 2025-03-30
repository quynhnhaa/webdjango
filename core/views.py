from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
from django.contrib.auth import authenticate, login, logout
import random
# Create your views here.


class HomeView(View):
    def get(self, request):

        # recipe_ids = Recipe.objects.values_list('id', flat=True)
        # random_ids = random.sample(list(recipe_ids), min(len(recipe_ids), 8))
        # random_recipes = Recipe.objects.filter(id__in=random_ids)
        recipes = list(Recipe.objects.order_by('?'))  # Lấy danh sách ngẫu nhiên
        while len(recipes) < 8:
            recipes.append(random.choice(recipes))  # Lặp lại ngẫu nhiên nếu chưa đủ
        context = {"random_recipes": recipes[:8]}
        return render(request, "homepage/index.html", context)
class LoginView(View):
    template_name = "homepage/login.html"

    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("pass")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("core:index")
        else:
            return render(request, self.template_name, {"error": "Tên đăng nhập hoặc mật khẩu sai"})
        
class LogoutView(View):
    def get(self, request):
        logout(request) 
        return redirect("core:index")  