from django.contrib import admin

# Register your models here.
from core.models import Meal, Category, Recipe

admin.site.register(Meal)
admin.site.register(Category)
admin.site.register(Recipe)
