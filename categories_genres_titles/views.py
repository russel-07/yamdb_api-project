from django.db.models import Avg
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, ReadTitleSerializer, WriteTitleSerializer
from .permissions import IsAdminOrReadOnly
from .filters import TitleFilter


class SampleViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                    mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryViewSet(SampleViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(SampleViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score')).order_by('-id')
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadTitleSerializer
        return WriteTitleSerializer

