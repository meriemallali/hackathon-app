
from rest_framework import serializers
from .models import *


# user profile serializer.
class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = UserProfile
        fields = ['username', 'email',
                  'first_name', 'last_name', 'profile_status', 'profile_photo']