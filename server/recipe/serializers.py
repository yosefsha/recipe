"""
Serializers for recipe API
"""
from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe list"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price']
        read_only_fields = ['id']


class RecipeDetailSerializer(serializers.ModelSerializer):
    """Serializer for recipe detail"""

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'time_minutes', 'price', 'user']
        read_only_fields = ['id', 'user']