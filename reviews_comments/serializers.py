from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, slug_field='username', read_only=True)
    #title = serializers.SlugRelatedField(many=False, slug_field='id', read_only=True)

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review