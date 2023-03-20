from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet


router = DefaultRouter()
router.register('v1/categories', CategoryViewSet, basename='Category')
router.register('v1/genres', GenreViewSet, basename='Genre')
router.register('v1/titles', TitleViewSet, basename='Title')


urlpatterns = [
    path('', include(router.urls)),
]

