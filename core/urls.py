from django.urls import path
from core import views


urlpatterns = [
    path('', views.IndexListView.as_view(), name='home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('<int:recipe_pk>/', views.recipe_detail_view, name='recipe-detail'),
    path('pantry/', views.pantry_view, name='pantry'),
    path('general principles/', views.general_principles_view, name='general-principles'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", views.SignUpView.as_view(), name="signup"),

]