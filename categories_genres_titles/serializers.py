from rest_framework import serializers
from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre


class ReadTitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
    rating = serializers.IntegerField()

    class Meta:
        fields = ['id', 'name', 'year', 'rating', 'description', 'genre', 'category']
        model = Title


class WriteTitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), many=False, slug_field='slug')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), many=True, slug_field='slug')
    rating = serializers.IntegerField(default=None, read_only=True)
    class Meta:
        fields = ['id', 'name', 'year', 'rating', 'description', 'genre', 'category']
        model = Title