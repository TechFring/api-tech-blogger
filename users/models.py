from django.contrib.auth.models import AbstractUser
from django.db import models

from publications.utils import get_filepath


class User(AbstractUser):
    email = models.EmailField(unique=True)
    photo = models.ImageField(default=None, blank=True, upload_to=get_filepath)
    total_publications = models.IntegerField(default=0)
    bio = models.TextField(blank=True, max_length=255)
