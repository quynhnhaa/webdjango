from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from recipes.models import Recipe
from reviews.models import Review
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

        # Lưu thông báo vào session
        request.session["recipe_message"] = "Đã Đăng"
        request.session["recipe_status"] = "success"

        return redirect("recipes:recipe_detail", recipe_id=recipe_id)