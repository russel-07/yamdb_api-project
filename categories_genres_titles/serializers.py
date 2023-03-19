from rest_framework import serializers
from .models import Categorie, Genre, Title


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Categorie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'year', 'rating', 'description', 'genre', 'category']
        models = Title