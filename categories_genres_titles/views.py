from rest_framework import viewsets, mixins, filters

from .models import Categorie, Genre, Title
from .serializers import CategorieSerializer, GenreSerializer, TitleSerializer
from .permissions import IsAdminOrReadOnly


class SampleViewSet(mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategorieViewSet(SampleViewSet):
    serializer_class = CategorieSerializer
    queryset = Categorie.objects.all()


class GenreViewSet(SampleViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()





