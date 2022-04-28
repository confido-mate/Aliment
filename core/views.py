from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, TemplateView, DetailView, CreateView

from core.filters import RecipeFilter
from core.models import Recipe, Ingredient, Shopping


# Create your views here.
class IndexListView(ListView):
    model = Recipe
    queryset = Recipe.objects.all()[:4]
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecipeListView(ListView):
    paginate_by = 15
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context


# @login_required(login_url='/accounts/login/')
def recipe_detail_view(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)
    context = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split('.'),
        'instructions': recipe.instructions.split('.'),
        'hints': recipe.hints.split('.'),
    }
    return render(request, 'recipe_detail.html', context=context)


def pantry_view(request):
    context = {
        'ingredients': Ingredient.objects.all(),
        'shopping-list': Shopping.objects.all()
    }
    return render(request, 'pantry.html', context=context)


def general_principles_view(request):
    recipes = Recipe.objects.all()
    search_form = RecipeFilter(request.GET, queryset=recipes)
    recipes = search_form.qs
    context = {
        'recipes': recipes,
        'search_form': search_form
    }
    return render(request, 'general_principles.html', context=context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


'''
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context
        
        
def recipe_list_view(request):
    recipes = Recipe.objects.all()

    #  pagination
    paginator = Paginator(recipes, 15)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    # search query
    search_form = RecipeFilter(request.GET, queryset=recipes)
    recipes = search_form.qs

    context = {
        'recipes': recipes,
        'search_form': search_form,
        'page_object': page_object
    }
    return render(request, 'recipes.html', context=context)
        
        
class RecipeDetailView(DetailView):
    template_name = 'recipe_detail.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instructions'] = self.model.instructions.value_to_string().split('.')
        return context
'''
