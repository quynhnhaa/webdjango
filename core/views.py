from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
from django.contrib.auth import authenticate, login, logout
import random
from users.models import User
from django.contrib import messages
# Create your views here.


class HomeView(View):
    def get(self, request):
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
        
class RegisterView(View):
    def get(self, request):
        return render(request, "homepage/register.html")
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên tài khoản đã được sử dụng!")
            return render(request, 'homepage/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng!")
            return render(request, 'homepage/register.html')

        if password1 != password2:
            messages.error(request, "Mật khẩu xác nhận không khớp!")
            return render(request, 'homepage/register.html')

    
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('core:login') 
class LogoutView(View):
    def get(self, request):
        logout(request) 
        return redirect("core:index")  