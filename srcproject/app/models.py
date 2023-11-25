from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from datetime import datetime
import uuid


# To store user's data.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    userid = models.IntegerField()
    profile_status = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profile/', default='blankprofile.jpg')

    def __str__(self):
        return self.user.username


# to stores the Recipes
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='recipephotos/', blank=True, null=True)
    posted_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
