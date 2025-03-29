from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Recipe)
admin.site.register(models.Category)
admin.site.register(models.Ingredient)
admin.site.register(models.RecipeIngredient)