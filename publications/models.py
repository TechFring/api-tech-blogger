from uuid import uuid4

from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from users.models import User

from .utils import get_filepath


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, verbose_name="nome")
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="criado em"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="atualizado em")

    class Meta:
        db_table = "tags"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Publication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="usuário"
    )
    title = models.CharField(max_length=50, verbose_name="título")
    subtitle = models.CharField(max_length=150, verbose_name="subtítulo")
    cover = models.ImageField(default=None, upload_to=get_filepath, verbose_name="capa")
    content = models.TextField(verbose_name="conteúdo")
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="criado em"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="atualizado em")

    class Meta:
        verbose_name = "publicação"
        verbose_name_plural = "publicações"
        db_table = "publications"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Saved(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, verbose_name="publicação"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="usuário"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="criado em"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="atualizado em")

    class Meta:
        verbose_name = "salvo"
        verbose_name_plural = "salvos"
        db_table = "saved"
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                fields=["publication", "user"], name="publication_and_user_uniq"
            )
        ]

    def __str__(self):
        return str(self.id)


@receiver((post_save, post_delete), sender=Publication)
def get_total_publications(sender, instance, *args, **kwargs):
    total = Publication.objects.filter(user_id=instance.user_id).count()
    user = User.objects.get(id=instance.user_id)
    user.total_publications = total
    user.save(update_fields=["total_publications"])


@receiver(post_delete, sender=Publication)
def remove_image_file(sender, instance, *args, **kwargs):
    instance.cover.delete(save=False)
