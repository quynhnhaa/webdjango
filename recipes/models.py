from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True) # meal_type

    def __str__(self):
        return self.name
    
class DetailCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  

    class Meta:
        unique_together = ('name', 'category')
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    cook_time = models.IntegerField(blank=True, null=True)  # Thời gian nấu (phút)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=10, blank=True, null=True)  # Độ khó (dễ, trung bình, khó)
    servings = models.IntegerField(blank=True, null=True)  # Số phần ăn

    category = models.ManyToManyField(DetailCategory)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    
    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)  # Ví dụ: "200g", "1 muỗng cà phê"

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} cho {self.recipe.name}"
