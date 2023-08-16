from rest_framework import serializers

from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review

    def validate(self, attrs):
        author = self.context['request'].user
        title = self.context['view'].kwargs.get('title_id')
        message = 'Author review already exist'
        if not self.instance and Review.objects.filter(author=author,
                                                       title=title).exists():
            raise serializers.ValidationError(message)
        return attrs


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(many=False, slug_field='username',
                                          read_only=True)

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        model = Comment
