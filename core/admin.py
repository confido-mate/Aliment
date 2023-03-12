from django.contrib import admin

# Register your models here.
from core.models import Meal, Category, Ingredient, Instruction, Recipe

admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(Recipe)
