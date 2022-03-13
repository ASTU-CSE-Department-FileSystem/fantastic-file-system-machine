from re import A
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Department, School

User = get_user_model()

class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('work info'), {'fields': ('department', 'type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'department', 'type')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department', 'school')
    list_filter = ('school',)
    search_fields = ('school', 'department')
    ordering = ('school', 'department')

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school',)
    list_filter = ('school',)
    search_fields = ('school',)
    ordering = ('school',)  

admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(School, SchoolAdmin)