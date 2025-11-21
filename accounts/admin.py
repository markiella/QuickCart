from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'total_orders', 'suki_points', 'is_active')
    list_filter = ('role', 'is_active', 'is_first_time_customer', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('role', 'phone_number', 'address', 'is_first_time_customer', 'suki_points', 'total_orders')
        }),
    )
