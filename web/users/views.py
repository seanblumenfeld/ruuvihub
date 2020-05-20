from django.contrib.auth import get_user_model
from rest_framework import viewsets

from web.users.serializers import UserSerializer

user_model = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = user_model.objects.all()
