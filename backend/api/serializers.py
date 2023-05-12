
from rest_framework import serializers
from .models import User, Table


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['title', 'description']
