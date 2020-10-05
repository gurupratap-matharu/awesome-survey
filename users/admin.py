from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', ]
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


admin.site.register(CustomUser, CustomUserAdmin)
