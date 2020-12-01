from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Account
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        refresh = RefreshToken.for_user(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED, headers=headers)
