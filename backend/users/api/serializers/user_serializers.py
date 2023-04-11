from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model, authenticate
from users.models import User
from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_name', 'image')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'name', 'last_name')

    def create(self, validate_data):
      """ Create a new User"""
      return get_user_model().objects.create_user(**validate_data)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name', 'phone', 'address', 'image')

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name', 'phone', 'address', 'image')

    # def create(self, validate_data):
    #   """ Create a new User"""
    #   return get_user_model().objects.create_user(**validate_data)