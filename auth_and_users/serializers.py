from rest_framework import serializers

from .models import User


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['email', 'confirmation_code']
        model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['first_name', 'last_name', 'username',
                  'bio', 'email', 'role']
        model = User
