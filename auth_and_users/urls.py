from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import Registration, EmailConfirmation, UserViewSet, UserRetrieveUpdate


router = DefaultRouter()
router.register('v1/users', UserViewSet)


urlpatterns = [
    path('v1/auth/email/', Registration.as_view()),
    path('v1/auth/token/', EmailConfirmation.as_view()),
    path('v1/users/me/', UserRetrieveUpdate.as_view(), name='User'),
    path('', include(router.urls)),
]

