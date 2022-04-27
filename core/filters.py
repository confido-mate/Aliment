from django_filters import FilterSet
from core.models import Recipe


class RecipeFilter(FilterSet):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'meal']