from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from .models import Recipe, Ingredient, Category, RecipeIngredient
import json
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.


class ViewIndex(View):
    def get(self, request):
        return HttpResponse("HELOO")


class RecipeDetail(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        instructions = json.loads(recipe.instructions)
        reviews = recipe.review_set.all()
        context = {"recipe": recipe, "instructions": instructions, "reviews": reviews}
        return render(request, "recipes/recipe_detail.html", context)  


class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()  
        paginator = Paginator(recipes, 3)  

        page_number = request.GET.get("page")  # Lấy số trang từ URL (?page=2)
        page_obj = paginator.get_page(page_number)  # Lấy trang tương ứng

        context = {
            "recipes": page_obj,  # Danh sách món ăn của trang hiện tại
            "page_obj": page_obj,  # Đối tượng phân trang
        }
        return render(request, "recipes/recipe_list.html", context)
        # return render(request, "recipes/recipe_list.html")

class RecipeListSearchName(View):
    def get(self, request):
        recipes = Recipe.objects.all()  #Viết hàm trả về danh sách recipes có tên tìm kiếm
        paginator = Paginator(recipes, 3)  

        page_number = request.GET.get("page")  # Lấy số trang từ URL (?page=2)
        page_obj = paginator.get_page(page_number)  # Lấy trang tương ứng

        context = {
            "recipes": page_obj,  # Danh sách món ăn của trang hiện tại
            "page_obj": page_obj,  # Đối tượng phân trang
        }
        return render(request, "recipes/recipe_list.html", context)
        
class RecipeListSearchCategory(View):
    def get(self, request):
        recipes = Recipe.objects.all()  #Viết hàm trả về danh sách recipes có tên tìm kiếm
        paginator = Paginator(recipes, 3)  

        page_number = request.GET.get("page")  # Lấy số trang từ URL (?page=2)
        page_obj = paginator.get_page(page_number)  # Lấy trang tương ứng

        context = {
            "recipes": page_obj,  # Danh sách món ăn của trang hiện tại
            "page_obj": page_obj,  # Đối tượng phân trang
        }
        return render(request, "recipes/recipe_list.html", context)
        

class RecipeCreate(View):
    def get(self, request):
        # Chuyển QuerySet thành danh sách
        ingredients = list(Ingredient.objects.values_list('name', flat=True))  # Lấy danh sách tên nguyên liệu
        categorys = list(Category.objects.values_list('name', flat=True))  # Lấy danh sách tên danh mục
        context = {"ingredients": ingredients, "categorys": categorys}
        return render(request, "recipes/recipe_create.html", context)

    def post(self, request):
        # Lấy dữ liệu cơ bản
        name = request.POST.get('name')
        description = request.POST.get('description')
        cooking_time = request.POST.get('cooking_time')
        image = request.FILES.get('image')
        category_name = request.POST.get('category', '')
        ingredients_raw = request.POST.get('ingredients', '[]')
        steps_raw = request.POST.get('steps', '[]')

        # Xử lý JSON an toàn
        try:
            ingredients = json.loads(ingredients_raw) if ingredients_raw else []
            steps = json.loads(steps_raw) if steps_raw else []
        except json.JSONDecodeError:
            ingredients = []
            steps = []

        # Kiểm tra dữ liệu bắt buộc
        if not name or not cooking_time or not steps:
            return HttpResponse("Thiếu dữ liệu bắt buộc: tên món, thời gian nấu hoặc các bước.", status=400)

        # Chuyển cooking_time thành integer
        try:
            cooking_time = int(cooking_time)
            if cooking_time <= 0:
                raise ValueError("Thời gian nấu phải là số dương.")
        except ValueError:
            return HttpResponse("Thời gian nấu phải là một số nguyên dương.", status=400)
        
        # Xử lý danh mục (Category)
        category = None
        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)

        # Tạo instructions từ steps dưới dạng JSON
        instructions_list = [
            {"step": i + 1, "instruction": step["description"]}
            for i, step in enumerate(steps)
        ]
        instructions = json.dumps(instructions_list, ensure_ascii=False)  

        # Lấy user hiện tại (nếu có đăng nhập)
        author = request.user if request.user.is_authenticated else None

        # Tạo Recipe
        recipe = Recipe(
            name=name,
            description=description,
            instructions=instructions,  
            cook_time=cooking_time,
            image=image,
            category=category,
            author=author
        )
        recipe.save()
        # Xử lý Ingredients và RecipeIngredient
        for item in ingredients:
            ingredient_name = item.get('name')
            quantity = item.get('quantity')
            
            if not ingredient_name or not quantity:
                continue  # Bỏ qua nếu thiếu tên hoặc số lượng

            # Tạo hoặc lấy Ingredient
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)

            # Tạo RecipeIngredient
            RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                quantity=quantity
            )
        # Lưu thông báo vào session
        request.session["recipe_success"] = True

        return redirect("recipes:recipe_detail", recipe_id=recipe.id)
    
def clear_recipe_success(request):
    request.session.pop("recipe_success", None)
    return JsonResponse({"status": "success"})


class ShowImage(View):
    def get(self, request):
        r = Recipe.objects.get(pk=2)
        return render(request, "recipes/image.html", {"r": r})