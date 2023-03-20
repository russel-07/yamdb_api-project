from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet


router = DefaultRouter()
router.register(r'v1/titles/(?P<id>[0-9]+)/reviews', ReviewViewSet, basename='Review')


urlpatterns = [
    path('', include(router.urls)),
]