from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'get_total_items', 'get_total_price', 'created_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'session_key')
    inlines = [CartItemInline]
    
    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Total Items'
    
    def get_total_price(self, obj):
        return f"₱{obj.get_total_price():.2f}"
    get_total_price.short_description = 'Total Price'
