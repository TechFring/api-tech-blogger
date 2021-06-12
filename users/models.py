from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from publications.utils import get_filepath


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    photo = models.ImageField(default=None, blank=True, upload_to=get_filepath)
    total_publications = models.IntegerField(default=0)
    bio = models.TextField(blank=True)


class Follower(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="follower", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "seguidor"
        verbose_name_plural = "seguidores"
        db_table = "followers"
        ordering = ("created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=["user", "follower"], name="user_and_follower_unique"
            )
        ]

    def __str__(self):
        return str(self.follower)
