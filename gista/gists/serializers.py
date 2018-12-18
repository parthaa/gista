from rest_framework import serializers
from .models import Gist
from django.contrib.auth.models import User


class GistSerializer(serializers.ModelSerializer):
    class Meta:
      model = Gist
      fields = ('id', 'created', 'modified', 'author', 'body','language')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ('id', 'username', 'first_name', 'last_name', 'email')
