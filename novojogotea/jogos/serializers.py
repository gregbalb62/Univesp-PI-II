from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MemoryGame

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MemoryGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryGame
        fields = ['id', 'score', 'level', 'date', 'user']
