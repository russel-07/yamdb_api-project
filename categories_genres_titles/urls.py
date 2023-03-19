from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategorieViewSet, GenreViewSet


router = DefaultRouter()
router.register('v1/categories', CategorieViewSet, basename='Categorie')
router.register('v1/genres', GenreViewSet, basename='Genre')


urlpatterns = [
    path('', include(router.urls)),
]

