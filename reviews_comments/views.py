from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAuthorOrModeratorOrAdminOrReadOnly, IsAuthorOrReadOnly
from categories_genres_titles.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrModeratorOrAdminOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('id'))
        return title.reviews.all()

