from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from .models import User
from django.contrib import auth
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.create(user=user)
        auth.login(request, user)
        return Response({"status":f"{token}"}, status=status.HTTP_202_ACCEPTED)

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response({"status":"success"}, status=status.HTTP_202_ACCEPTED)

from .serializers import RegisterSerializer
from rest_framework import generics


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer