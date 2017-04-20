from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    email = models.EmailField(null=False)


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_url = models.CharField(max_length=500, null=True, blank=True)
    avatar_file_name = models.CharField(max_length=500, null=True, blank=True)