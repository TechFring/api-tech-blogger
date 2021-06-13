from django.contrib import admin

from .models import Publication, Saved, Tag


# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    fields = ("name",)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "subtitle", "created_at", "updated_at")
    fields = ("user", "title", "subtitle", "content", "tags", "cover")


@admin.register(Saved)
class SavedAdmin(admin.ModelAdmin):
    list_display = ("publication", "user", "created_at", "updated_at")
    fields = ("publication", "user")
