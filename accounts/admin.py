from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, UserType
from django.utils.translation import gettext, gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = UserProfile 
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', )}),#'usertype'
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(UserProfile, CustomUserAdmin)
admin.site.register(UserType)