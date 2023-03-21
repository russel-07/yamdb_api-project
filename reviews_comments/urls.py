from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReviewViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'v1/titles/(?P<id>[0-9]+)/reviews', ReviewViewSet, basename='Review')
router.register(r'v1/titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments', CommentViewSet, basename='Comment')


urlpatterns = [
    path('', include(router.urls)),
]