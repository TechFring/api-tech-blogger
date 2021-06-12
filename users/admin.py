from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Follower

# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("bio", "photo")}),
    )


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("user", "follower", "created_at", "updated_at")
    fields = ("user", "follower")
