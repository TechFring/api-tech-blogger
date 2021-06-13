from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = (
        "username",
        "first_name",
        "total_publications",
        "is_staff",
        "is_superuser",
    )
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("bio", "photo")}),
    )
