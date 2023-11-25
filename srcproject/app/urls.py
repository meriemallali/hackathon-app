from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name="feed"),
    path('login', views.login_user, name="login"),
    path('register', views.register, name="signup"),
    path('logout', views.logout, name="logout"),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('search-recipe/', views.search_recipe, name='search-recipe'),
]
