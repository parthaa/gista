from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GistSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Gist


class GistView(viewsets.ModelViewSet):
    queryset = Gist.objects.all()
    serializer_class = GistSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
