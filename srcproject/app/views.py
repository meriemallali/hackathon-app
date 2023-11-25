from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .forms import *
from .models import *
from itertools import chain
from .models import Recipe
from .forms import RecipeForm


# url: ''
# @desc: return all recipes in the db
def feed(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        print(recipe.photo.url)

    return render(request, 'feed.html', {'recipes': recipes})


# url: 'register'
# @desc: for users to register to the platform.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmedpassword = request.POST['confirmedpassword']
        # comparing the passwords, if match then check if user exists by email or username.
        # if not, register the new user and create its profile.
        if password == confirmedpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken, try with different one.')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()

                # log user in
                logged_user = auth.authenticate(username=username, password=password)
                auth.login(request, logged_user)

                # create the profile for the new user
                new_userProfile = UserProfile.objects.create(user=User.objects.get(username=username),
                                                             userid=User.objects.get(username=username).id)
                new_userProfile.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match. Re-enter password.')
            return redirect('register')
    else:
        return render(
            request, 'register.html')


# url: 'login'
# @desc: only registered users can sign in.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        registered_user = authenticate(username=username, password=password)
        if registered_user:
            if registered_user.is_active:
                login(request, registered_user)
                return redirect('/')
            else:
                messages.info(request, 'Your account has been disabled.')
        else:
            messages.info(request, 'Invalid login details.')

    else:
        return render(request, 'login.html')

    return render(request, 'login.html')


# url: 'logout'
# description: only log in user can log out.
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


# url: 'add_recipe/'
# @desc: add new recipes to the db.
@login_required(login_url='login')
def add_recipe(request):
    if request.method == 'POST':

        user = request.user
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        preparation_steps = request.POST.get('preparation_steps')
        preparation_time_str = request.POST.get('preparation_time')  # get as string

        try:
            preparation_time = int(preparation_time_str)
        except ValueError:
            return HttpResponseBadRequest("Preparation time must be a valid integer.")

        photo = request.FILES.get('photo')
        new_recipe = Recipe.objects.create(user=user, name=name, ingredients=ingredients,
                                           preparation_steps=preparation_steps, preparation_time=preparation_time,
                                           photo=photo)
        new_recipe.save()
    return render(request, 'add-recipe.html')


# url: 'search-recipe'
# @desc: return the list of searched recipes.
def search_recipe(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        search_object = Recipe.objects.filter(name__icontains=name)


        data = {
            'name': name,
            'search_result': search_object
        }

    return render(request, 'search-result.html', data)
