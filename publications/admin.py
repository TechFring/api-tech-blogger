from django.contrib import admin

from .models import Tag, Publication, Comment

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    fields = ("name",)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "subtitle", "created_at", "updated_at")
    fields = ("user", "title", "subtitle", "content", "tags", "cover")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("publication", "user", "content", "created_at", "updated_at")
    fields = ("publication", "user", "content")
