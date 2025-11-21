from django.contrib import admin
from .models import PromoCode, SukiDiscount, FirstTimeCustomerPromo, DiscountUsage

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'usage_count', 'usage_limit', 'is_active', 'valid_from', 'valid_until')
    list_filter = ('discount_type', 'is_active', 'valid_from', 'valid_until')
    search_fields = ('code', 'description')
    readonly_fields = ('usage_count',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('code', 'description', 'is_active')
        }),
        ('Discount Configuration', {
            'fields': ('discount_type', 'discount_value', 'minimum_order_amount', 'maximum_discount_amount')
        }),
        ('Usage Limits', {
            'fields': ('usage_limit', 'usage_count')
        }),
        ('Validity Period', {
            'fields': ('valid_from', 'valid_until')
        }),
    )

@admin.register(SukiDiscount)
class SukiDiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'minimum_orders', 'discount_percentage', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name',)

@admin.register(FirstTimeCustomerPromo)
class FirstTimeCustomerPromoAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_type', 'discount_value', 'is_active', 'valid_from', 'valid_until')
    list_filter = ('discount_type', 'is_active', 'valid_from', 'valid_until')
    search_fields = ('name',)

@admin.register(DiscountUsage)
class DiscountUsageAdmin(admin.ModelAdmin):
    list_display = ('user', 'discount_type', 'discount_amount', 'order_amount', 'used_at')
    list_filter = ('discount_type', 'used_at')
    search_fields = ('user__username', 'promo_code__code')
    readonly_fields = ('used_at',)
