from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from .models import Recipe, Ingredient, Category, RecipeIngredient
import json
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
import json
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from recipes.cf_models import global_cf_instance
# Create your views here.


class ViewIndex(View):
    def get(self, request):
        return HttpResponse("HELOO")


from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Recipe

class RecipeDetail(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)

        instructions = recipe.instructions.splitlines() if recipe.instructions else []

        reviews = recipe.review_set.all()

        recipe_categories = ', '.join(recipe.category.values_list('name', flat=True))

        # Lấy thông báo từ session (nếu có)
        recipe_message = request.session.pop("recipe_message", None)
        recipe_status = request.session.pop("recipe_status", None)
        
        #Đề xuất món ăn cho người dùng id
        if request.user.is_authenticated:
            id = request.user.id
            cf = global_cf_instance
            recommendations = cf.recommend(id) if cf else []
            recommended_ids = [item_id for item_id, score in recommendations]
            recipe_recommended = Recipe.objects.filter(id__in=recommended_ids)
        else:
            recipe_recommended = []
        # Truyền dữ liệu vào context để render ra template
        context = {
            "recipe": recipe,
            "instructions": instructions,
            "reviews": reviews,
            "recipe_categories" : recipe_categories,  
            "recipe_status": recipe_status,
            "recipe_message": recipe_message,
            "recipe_recommended": recipe_recommended
        }

        return render(request, "recipes/recipe_detail.html", context)


class RecipeListView(View):
    def get(self, request):
        query = request.GET.get("search", "").strip()
        selected_detailcategories = request.GET.getlist("detailcategory")
        selected_detailcategories = [str(id) for id in selected_detailcategories]

        personal = request.GET.get("personal", "-1")
        try:
            personal = int(personal)
        except ValueError:
            personal = -1

        recipes = Recipe.objects.all()

        # Lọc theo từ khóa
        if query:
            recipes = recipes.filter(name__icontains=query)

        # Lọc theo category (nếu là ForeignKey)
        if selected_detailcategories:
            for category_id in selected_detailcategories:
                recipes = recipes.filter(category__id=category_id)

        # Phân trang
        paginator = Paginator(recipes, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "recipes": page_obj,
            "page_obj": page_obj,
            "query": query,
            "selected_detailcategories": selected_detailcategories,
            "personal": personal,
        }
        return render(request, "recipes/recipe_list.html", context)


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
        
def get_create_or_edit_view(request, recipe_id=None):
    context = {}
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Kiểm tra quyền chỉnh sửa (nếu cần)
        if recipe.author != request.user and not request.user.is_admin:
            return HttpResponse("Bạn không có quyền chỉnh sửa recipe này.", status=403)
        context['recipe_detailcategory_ids'] = list(recipe.category.values_list("id", flat=True))
        
        # Parse instructions từ JSON sang list để hiển thị trong form
        context['instructions'] = json.loads(recipe.instructions) if recipe.instructions else []
        # Lấy danh sách RecipeIngredient
        context['recipe_ingredients'] = RecipeIngredient.objects.filter(recipe=recipe)
        context['recipe'] = recipe

    # Lấy danh sách category và ingredient để hiển thị trong datalist
    context['ingredients'] = list(Ingredient.objects.values_list('name', flat=True))

    return render(request, "recipes/recipe_edit.html", context=context)

def post_create_or_edit(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
        # Kiểm tra quyền chỉnh sửa
        if recipe.author != request.user and not request.user.is_admin:
            return HttpResponse("Bạn không có quyền chỉnh sửa recipe này.", status=403)

    # Lấy dữ liệu từ form
    name = request.POST.get('name')
    description = request.POST.get('description')
    cooking_time = request.POST.get('cooking_time')
    image = request.FILES.get('image')
    detail_category_ids = json.loads(request.POST.get('detailcategory_ids', '[]'))
    ingredients_raw = request.POST.get('ingredients', '[]')
    steps_raw = request.POST.get('steps', '[]')

    # Xử lý JSON
    try:
        ingredients = json.loads(ingredients_raw) if ingredients_raw else []
        steps = json.loads(steps_raw) if steps_raw else []
    except json.JSONDecodeError:
        ingredients = []
        steps = []

    # Kiểm tra dữ liệu bắt buộc
    if not name or not cooking_time or not steps:
        return HttpResponse("Thiếu dữ liệu bắt buộc.", status=400)

    # Chuyển cooking_time thành integer
    try:
        cooking_time = int(cooking_time)
        if cooking_time <= 0:
            raise ValueError
    except ValueError:
        return HttpResponse("Thời gian nấu phải là số nguyên dương.", status=400)


    # Cập nhật instructions
    instructions_list = [{"step": i + 1, "instruction": step["description"]} for i, step in enumerate(steps)]
    instructions = json.dumps(instructions_list, ensure_ascii=False)
    # Xử lý detail categories
    detail_category_ids = [int(id) for id in detail_category_ids if id != '']
    if recipe_id:
        # Cập nhật Recipe
        recipe.name = name
        recipe.description = description
        recipe.instructions = instructions
        recipe.cook_time = cooking_time
        if image:
            recipe.image = image
    else:
        # # Tạo Recipe
        author = request.user if request.user.is_authenticated else None
        recipe = Recipe(
            name=name,
            description=description,
            instructions=instructions,  
            cook_time=cooking_time,
            image=image,
            author=author
        )
    recipe.save()
    recipe.category.set(detail_category_ids)
    # Xóa RecipeIngredient cũ và thêm mới
    RecipeIngredient.objects.filter(recipe=recipe).delete()
    for item in ingredients:
        ingredient_name = item.get('name')
        quantity = item.get('quantity')
        if ingredient_name and quantity:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient, quantity=quantity)

    # Lưu thông báo vào session
    mess = 'cập nhật' if recipe_id else 'tạo'
    request.session["recipe_message"] = f"Bạn đã {mess} món ăn thành công!"
    request.session["recipe_status"] = "success"

    return redirect("recipes:recipe_detail", recipe_id=recipe.id)


def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Kiểm tra quyền sở hữu (nếu cần)
    if recipe.author != request.user:
        messages.error(request, "Bạn không có quyền xóa công thức này!")
        return redirect("recipes:recipe_list")

    recipe.delete()
    messages.success(request, "Công thức đã được xóa thành công!")

    # Lấy URL trước đó từ request
    next_url = request.GET.get("next", "recipes:recipe_list")
    return HttpResponseRedirect(next_url)

class RecipeCreate(View):
    
    def get(self, request):
        return get_create_or_edit_view(request)

    def post(self, request):
        return post_create_or_edit(request)

class RecipeEdit(View):
    def get(self, request, recipe_id=None):
        return get_create_or_edit_view(request, recipe_id=recipe_id)
    
    def post(self, request, recipe_id=None):
        return post_create_or_edit(request, recipe_id=recipe_id)
    
# class RecipePersonal(View):
#     def get(self, request):
#         recipes = Recipe.objects.filter(author=request.user)
#         context = pagination(request, recipes)
#         context["user"] = request.user
#         return render(request, "recipes/recipe_personal.html", context)


def clear_recipe_success(request):
    request.session.pop("recipe_success", None)
    return JsonResponse({"status": "success"})


def pagination(request, recipes):
    paginator = Paginator(recipes, 3)  

    page_number = request.GET.get("page")  # Lấy số trang từ URL (?page=2)
    page_obj = paginator.get_page(page_number)  # Lấy trang tương ứng

    context = {
        "recipes": page_obj,  # Danh sách món ăn của trang hiện tại
        "page_obj": page_obj,  # Đối tượng phân trang
    }
    return context

class ShowImage(View):
    def get(self, request):
        r = Recipe.objects.get(pk=2)
        return render(request, "recipes/image.html", {"r": r})