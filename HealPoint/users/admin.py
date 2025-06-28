from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserHealPoint

class UserHealPointAdmin(BaseUserAdmin):
    ordering = ['phone_number']
    list_display = ['phone_number', 'is_admin', 'is_active']
    search_fields = ['phone_number']
    
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )

admin.site.register(UserHealPoint, UserHealPointAdmin)
