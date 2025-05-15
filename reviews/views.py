from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
from reviews.models import Review
from recipes.cf_models import global_cf_instance
import numpy as np
# Create your views here.


class ViewIndex(View):
    def get(self, request):
        return HttpResponse("HELOO")
    
class ReviewCreate(View):
    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        user = request.user
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        # Tạo review mới
        review = Review.objects.create(
            recipe=recipe,
            user=user,
            rating=int(rating),  # Ví dụ: đánh giá 5 sao
            comment=comment
        )
        #Thêm rating vào danh sách của recomender
        cf = global_cf_instance
        cf.add(np.array([[user.id, recipe.id, int(rating)]]))
        # Lưu thông báo vào session
        request.session["recipe_message"] = "Đã Đăng"
        request.session["recipe_status"] = "success"

        return redirect("recipes:recipe_detail", recipe_id=recipe_id)