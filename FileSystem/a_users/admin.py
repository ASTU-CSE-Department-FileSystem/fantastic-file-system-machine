from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from .models import Department, School

User = get_user_model()

admin.site.register((User, School, Department))