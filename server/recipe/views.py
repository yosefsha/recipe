"""
Views for the recipe APIs
"""
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe.serializers import (
    RecipeSerializer,
    RecipeDetailSerializer
)


class RecipeListView(generics.ListAPIView):
    """List all recipes for authenticated user"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')


class RecipeDetailView(generics.RetrieveAPIView):
    """Retrieve a recipe by id"""
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user)


class RecipeCreateView(generics.CreateAPIView):
    """Create a new recipe"""
    serializer_class = RecipeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Create a new recipe for authenticated user"""
        serializer.save(user=self.request.user)