
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = User
    #specify what informatioin is shown on the admin page
    list_display = ['email','first_name']

admin.site.register(User, CustomUserAdmin)