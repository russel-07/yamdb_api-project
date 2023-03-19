from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework import views, generics, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin


class Registration(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.data.get('email')
        user, created = User.objects.get_or_create(email=email)
        confirmation_code = default_token_generator.make_token(user)
        user.confirmation_code = confirmation_code
        user.save()
        self.send_confirmation_code(email, confirmation_code)
        return Response({'email': email})
    
    def send_confirmation_code(self, email, confirmation_code):
        subject = 'Confirmation code from YamDb'
        message = f'Your confirmation code: {confirmation_code}'
        from_email = None
        to_email = [email]
        fail_silently=False
        send_mail(subject, message, from_email, to_email, fail_silently)


class EmailConfirmation(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)
        confirmation_code = request.data.get('confirmation_code')
        if user.confirmation_code == confirmation_code:
            token = self.get_token_for_user(user)
            return Response({'token': token})
        return Response({'message': 'Неверный код подтверждения.'})
    
    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    

class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


