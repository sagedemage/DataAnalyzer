
from rest_framework import serializers
from .models import User, Table, Row


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['name', 'column1_name', 'column2_name', 'user_id']


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['column1_data', 'column2_data', 'table_id']
