from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Gist(TimeStampedModel):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="gists")
  body = models.TextField(null=True, blank=True)
  language = models.TextField(null=True, blank=True)
