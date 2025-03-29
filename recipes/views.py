from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Recipe
import json
from django.core.paginator import Paginator

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
        return render(request, "recipes/recipe_create.html")
    

class ShowImage(View):
    def get(self, request):
        r = Recipe.objects.get(pk=2)
        return render(request, "recipes/image.html", {"r": r})