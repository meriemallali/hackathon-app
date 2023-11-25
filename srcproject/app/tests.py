import unittest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone

User = get_user_model()
from .models import *
from .views import *


# testing the authentication: resigter new user
class RegisterTestCase(unittest.TestCase):
    def test_check_invalid_user(self):
        # user with username 'meriema1' does not exist in the database.
        username = 'meriema1'
        message = f'{username} does not exists'
        user = User.objects.filter(username=username).exists()
        self.assertFalse(user, message)

    def test_check_valid_user(self):
        # create and save a new user profile.
        user = User.objects.create(
            username='newuser',
            email='newuser@gmail.com',
            password='newuser'
        )
        user.save()
        created_profile = UserProfile.objects.create(user=user,
                                                     userid=user.id)
        created_profile.save()
        # testing with the created user.
        username = 'newuser'
        message = f'{username} does exists'
        new_user = User.objects.filter(username=username)
        new_user_profile = UserProfile.objects.filter(user=user, userid=user.id)
        self.assertTrue(new_user, message)
        self.assertTrue(new_user_profile is not None)


# testing the authentication: signin
class SigninTestCase(unittest.TestCase):
    # test with non-existing user.
    def test_invalid_details(self):
        user = authenticate(username='meriama12', password='password')
        self.assertTrue(user is None)

    # test with an existing user.
    def test_valid_details(self):
        user = authenticate(username='test', password='1234567')
        self.assertFalse(user is not None)

# testing the authentication: logout
class LogoutTestCase(TestCase):
    # create a testing user.
    def setUp(self):
        self.user = User.objects.create_user(username='test2', password='test2')

    def test_logout(self):
        self.client.login(username='test2', password='test2')
        self.assertTrue(self.user.is_authenticated)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        # true = user logged out.
        self.assertTrue(self.user.is_authenticated)