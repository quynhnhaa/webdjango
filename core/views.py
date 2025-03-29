from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class HomeView(View):
    def get(self, request):
        recipe = Recipe.objects.first() 
        return render(request, "homepage/index.html", {"recipe": recipe})
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