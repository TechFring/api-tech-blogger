from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models

from publications.utils import get_filepath


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo = models.ImageField(default=None, blank=True, upload_to=get_filepath)
    total_publications = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
