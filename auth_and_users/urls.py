
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserRetrieveUpdate


router = DefaultRouter()
router.register('v1/users', UserViewSet)


urlpatterns = [
    path('v1/auth/token/', TokenObtainPairView.as_view()),
    path('v1/users/me/', UserRetrieveUpdate.as_view(), name='User'),
    path('', include(router.urls)),
]

